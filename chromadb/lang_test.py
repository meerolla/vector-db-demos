from dotenv import load_dotenv 
load_dotenv()

from langchain_openai import ChatOpenAI

model = ChatOpenAI(model="gpt-4")

print(model.invoke("What is AI"))