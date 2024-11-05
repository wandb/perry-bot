import weave  # type: ignore
import signal
import sys
import asyncio
from perry_model import StatefulPerryAdapter

def signal_handler(sig, frame):
    print("\nGoodbye!")
    sys.exit(0)

def chat():
    # Set up Ctrl+C handler
    signal.signal(signal.SIGINT, signal_handler)
    
    model = StatefulPerryAdapter()

    print("Perry ready. Press Ctrl+C to exit.")
    
    async def chat_loop():
        while True:
            try:
                user_input = input("User: ")
                if user_input.lower() == "exit":
                    print("Goodbye!")
                    break
                response = await model.predict(user_input)
                
                # Format the response based on type
                if isinstance(response, dict):
                    print("Assistant: Function call:", response)
                else:
                    print("Assistant:", response)
                    
            except EOFError:
                # Handle Ctrl+D
                print("\nGoodbye!")
                weave.finish()
                break

    asyncio.run(chat_loop())

if __name__ == "__main__":
    weave.init(project_name="perry")
    chat()
