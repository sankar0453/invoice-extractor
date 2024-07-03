from langchain_core.pydantic_v1 import BaseModel, Field
from langchain_community.document_loaders import PyPDFLoader
# from typing import Listpy
from dotenv import load_dotenv
import os
import google.generativeai as genai
from langchain_google_genai import ChatGoogleGenerativeAI
from typing import List
from PyPDF2 import PdfReader
# from langchain_google_vertexai import ChatVertexAI
from langchain_mistralai.chat_models import ChatMistralAI

load_dotenv()


genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text

class CVDataExtraction(BaseModel):
    username: str = Field(description="candidate username")
    email: str = Field(description="candidate email")
    profile: str = Field(description="candidate profile description")
    skills: List[str] = Field(description="soft and technical skills")
    
# Initialize the model
# model = ChatGoogleGenerativeAI(model="gemini-pro", temperature=0.3)
# model = genai.GenerativeModel('gemini-pro')
# model = ChatVertexAI(model="gemini-pro", temperature=0)
model = ChatMistralAI(api_key="", model='mistral-large-latest')
structured_llm = model.with_structured_output(CVDataExtraction)
pdf_text = get_pdf_text(["pdfparse/sample.pdf"])

    # Invoke the model with the extracted text
response = structured_llm.invoke(pdf_text)
print(response)

# if __name__ == "__main__":
#     # Extract text from the PDF
#     pdf_text = get_pdf_text(["pdfparse/sample.pdf"])

#     # Invoke the model with the extracted text
#     structured_llm.invoke(pdf_text)

