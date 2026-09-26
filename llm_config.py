from dotenv import load_dotenv
#import the groq llm library
from langchain_groq import ChatGroq


# Load environment variables from .env
load_dotenv()

def create_llm():
    llm = ChatGroq(model="openai/gpt-oss-20b")
    return llm


