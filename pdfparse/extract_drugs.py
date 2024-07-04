from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.pydantic_v1 import BaseModel, Field
from typing import List
import os
from dotenv import load_dotenv

load_dotenv()
groq_api_key=os.getenv('GROQ_API_KEY')

chat = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    api_key=groq_api_key
)

class DRUGS(BaseModel):
    """Extract clinical and medical named entities"""
    drugs: List[str] = Field(description="Drug or chemical entity")


structured_llm = chat.with_structured_output(DRUGS)
text = """Marrow Infiltrating Lymphocytes - Non-Small Cell Lung Cancer (MILs™ - NSCLC) Alone or in Combination With Nivolumab With or Without Tadalafil in Locally Advanced and Unresectable or Metastatic NSCLC"""
resposnse = structured_llm.invoke(text)
print(resposnse)