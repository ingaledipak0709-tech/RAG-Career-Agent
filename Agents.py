from dotenv import load_dotenv
#import the groq llm library
from langchain_groq import ChatGroq


# Load environment variables from .env
load_dotenv()

#initialize the llm model
llm = ChatGroq(model="openai/gpt-oss-20b")

response=llm.invoke("What is Rag")
print(response.content)