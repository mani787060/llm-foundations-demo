# First of all, we must have an "OPENAI_API_KEY", then only we can run this code

from langchain_openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

llm = OpenAI(model='gpt-3.5-turbo-instruct')

result = llm.invoke('what is the capital of India')

print(result)


 
# by the way, it's(LLMs) now become the old fashion, 
# that's why now LangChain also prefers to use 'ChatModels' inspite of LLMs
