# Perry virtual assistant
This repo contains code to run and evaluate a virtual assistant named Perry. Perry is a virtual assistant made to run on a smartphone. Perry also happens to showcase the amazing capabilities of Weave, a lightweight toolkit for tracking and evaluating LLM applications, built by Weights & Biases.

# Environment setup
First, ensure you have Python >= 3.10 installed.

Then: 
- `pip install -r requirements.txt`
- `export OPENAI_API_KEY=...`
- `wandb login`

# Chat with perry
`python chat.py`

# Evaluate perry
`python eval.py`
