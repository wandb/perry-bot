import json
import weave  # type: ignore
import openai
from openai.types.chat import ChatCompletionMessageParam
from pydantic import Field  # type: ignore

from functions import function_definitions


class PerryModelBase(weave.Model):
    prompt: str = ""
    model: str = "gpt-4o-mini"

    def __init__(self) -> None:
        super().__init__()
        self.prompt = """
You are Perry, a virtual assistant focused on helping users control their device and complete everyday tasks. Your responses should be:

1. PRACTICAL & PRECISE
- Focus on actionable tasks that can be accomplished through device functions
- When you understand a request, respond with ONLY the tool call - no extra text
- For ambiguous requests, ask for specific missing information (e.g. "What time?" or "Which contact?")
- Never invent capabilities - stick to your defined tool set

2. NATURAL & HELPFUL
- If a request is unclear, ask clarifying questions naturally: "Would you like me to..."
- When declining unsupported requests, suggest available alternatives
- For complex requests, break them down into manageable steps
- Maintain a helpful tone while being direct and efficient

3. RESPONSE FORMATS
- For executable tasks: Return ONLY the tool call
- For missing information: Ask a single, specific question
- For unsupported requests: Briefly explain why, then suggest an alternative

4. TASK PRIORITIES
- Safety first - be cautious with potentially dangerous settings
- Prefer exact matches over approximate ones
- When multiple tools could apply, choose the most specific
- For ambiguous requests, ask for clarification rather than guessing

5. KEY LIMITATIONS
- You cannot perform actions directly - you can only call defined tools
- You cannot access user data or previous conversations
- You cannot learn new tools or modify existing ones
- You cannot engage in general conversation or provide information outside your tool set

Remember: Your purpose is to help users efficiently control their device and complete tasks. Stay focused on what you can do rather than what you cannot.
"""

    @weave.op
    async def predict(self, thread: list[ChatCompletionMessageParam]) -> str | dict[str, str]:
        client = openai.AsyncOpenAI()
        messages: list[ChatCompletionMessageParam] = [
            {"role": "system", "content": self.prompt},
            *thread,
        ]
        output = await client.chat.completions.create(
            model=self.model,
            messages=messages,
            tools=function_definitions["functions"],  # type: ignore
        )

        if not output.choices or not output.choices[0].message:
            raise ValueError("No valid response received from the model.")

        message = output.choices[0].message

        # Check for tool calls first
        if message.tool_calls:
            tool_call = message.tool_calls[0]  # Take first tool call
            return {
                "function": tool_call.function.name,
                "parameters": json.loads(tool_call.function.arguments)
            }
        
        # Fall back to content if no tool calls
        if not message.content:
            raise ValueError("No content in model response")
            
        return message.content


class ChatThread:
    def __init__(self) -> None:
        self.messages: list[ChatCompletionMessageParam] = []

    def add_message(self, message: ChatCompletionMessageParam) -> None:
        self.messages.append(message)

    def get_messages(self) -> list[ChatCompletionMessageParam]:
        return self.messages


class StatefulPerryAdapter:
    perry_model: PerryModelBase = Field(default_factory=PerryModelBase)
    chat_thread: ChatThread = Field(default_factory=ChatThread)

    def __init__(self):
        super().__init__()
        self.perry_model = PerryModelBase()
        self.chat_thread = ChatThread()

    async def predict(self, request: str) -> str | dict:
        user_message: ChatCompletionMessageParam = {"role": "user", "content": request}
        self.chat_thread.add_message(user_message)

        response = await self.perry_model.predict(self.chat_thread.get_messages())

        # Handle both string and dict responses
        assistant_message: ChatCompletionMessageParam
        if isinstance(response, dict):
            # For tool calls, create a proper tool message
            assistant_message = {
                "role": "tool",
                "content": str(response),  # Convert dict to string for message history
                "tool_call_id": "fake_id",  # Simplified ID for history
            }
        else:
            assistant_message = {
                "role": "assistant",
                "content": response,
            }
        self.chat_thread.add_message(assistant_message)

        return response


class StatelessPerryAdapter(weave.Model):
    perry_model: PerryModelBase = Field(default_factory=PerryModelBase)

    def __init__(self):
        super().__init__()
        self.perry_model = PerryModelBase()
    
    @weave.op
    async def predict(self, user: str) -> str | dict:
        user_message: ChatCompletionMessageParam = {"role": "user", "content": user}
        response = await self.perry_model.predict([user_message])
        return response
