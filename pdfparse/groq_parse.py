from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain_core.pydantic_v1 import BaseModel, Field
import os
from dotenv import load_dotenv

load_dotenv()
groq_api_key=os.getenv('GROQ_API_KEY')

chat = ChatGroq(
    temperature=0,
    model="llama3-70b-8192",
    api_key=groq_api_key
)

class Joke(BaseModel):
    """Joke to tell user."""

    setup: str = Field(description="The setup of the joke")
    punchline: str = Field(description="The punchline to the joke")
    # rating: Optional[int] = Field(description="How funny the joke is, from 1 to 10")


structured_llm = chat.with_structured_output(Joke)

resposnse = structured_llm.invoke("Tell me a joke about cats")
print(resposnse)