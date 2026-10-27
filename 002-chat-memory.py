import os
from dotenv import load_dotenv, find_dotenv
# Remember: the .env file in the project folder must contain the line
# OPENAI_API_KEY=... (without quotes or spaces).
_ = load_dotenv(find_dotenv())
openai_api_key = os.environ["OPENAI_API_KEY"]

from langchain_openai import ChatOpenAI

# Original version: this example used gpt-3.5-turbo-0125.
# OpenAI has since retired it (shutdown on October 23, 2026).
# Today we use a current chat model: gpt-6-luna, small, fast and affordable.
# (This example does not call the model: the messages below are written by hand.)
MODEL = "gpt-6-luna"

# This version of langchain-openai sends temperature=0.7 by default,
# but recent OpenAI models only accept the default value (1).
# That is why we set temperature=1 explicitly.
llm = ChatOpenAI(model=MODEL, temperature=1)

# Original version: from langchain.memory import ChatMessageHistory
# That import still works, but it shows a LangChainDeprecationWarning:
# ChatMessageHistory now lives in the langchain_community package, which is
# already installed with this project. Importing it from there works the
# same way and shows no warning.
from langchain_community.chat_message_histories import ChatMessageHistory

history = ChatMessageHistory()

history.add_user_message("hi!")

history.add_ai_message("whats up?")

my_chat_memory = history.messages

print("\n----------\n")

print("Chat Memory:")

print("\n----------\n")
print(my_chat_memory)

print("\n----------\n")
