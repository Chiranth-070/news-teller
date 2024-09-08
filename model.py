#verify model is working fine
#you can use other models by reffering langchain documentation

from dotenv import load_dotenv
import os
from langchain_nvidia_ai_endpoints import ChatNVIDIA


load_dotenv()
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANG_CHAIN")
os.environ["NVIDIA_API_KEY"] = os.getenv("NVIDIA_API_KEY")

llm = ChatNVIDIA(model="meta/llama3-70b-instruct")

result = llm.invoke("Hello, how are you?")

print(result)