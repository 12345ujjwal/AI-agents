from strands import Agent
from strands.models.ollama import OllamaModel

model = OllamaModel(
    model_id="gemma4:31b-cloud",
    host="http://127.0.0.1:11434"
    )

agent = Agent(
    model=model,
    system_prompt="""You are a helpful assistant to chat in friendly way with user."""
)
while True:
    user_input = input("\nUser: ")
    agent(user_input)
