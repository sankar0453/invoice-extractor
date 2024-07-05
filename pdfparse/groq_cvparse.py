from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.pydantic_v1 import BaseModel, Field
from PyPDF2 import PdfReader
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

def get_pdf_text(pdf_docs):
    text=""
    for pdf in pdf_docs:
        pdf_reader= PdfReader(pdf)
        for page in pdf_reader.pages:
            text+= page.extract_text()
    return  text

class CVDataExtraction(BaseModel):
    """ATS Resume EXpert"""
    username: str = Field(description="candidate username")
    email: str = Field(description="candidate email")
    profile: str = Field(description="candidate profile description")
    skills: List[str] = Field(description="soft and technical skills")


structured_llm = chat.with_structured_output(CVDataExtraction)
pdf_text = get_pdf_text(["pdfparse/sample.pdf"])
pdf_text1="""
SKILLS
ALGORITHMS (1 year), APACHE (1 year), JAVA (1 year), SCRIPTING (1 year), API (Less than 1
year)."""
resposnse = structured_llm.invoke(pdf_text1)
print(resposnse)
# username='' email='' profile='' skills=['ALGORITHMS', 'APACHE', 'JAVA', 'SCRIPTING', 'API']