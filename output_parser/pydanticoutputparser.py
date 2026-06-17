from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import PydanticOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from pydantic import BaseModel, Field

# 1️⃣ Load environment variables (API key)
load_dotenv()

# 2️⃣ Initialize the Gemini model
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite"
)

# 3️⃣ Define output structure using Pydantic
class Person(BaseModel):
    name: str = Field(description="Name of the person")
    age: int = Field(description="Age of the person")
    city: str = Field(description="City the person belongs to")

# 4️⃣ Create a Pydantic output parser
parser = PydanticOutputParser(pydantic_object=Person)

# 5️⃣ Create prompt template
template = PromptTemplate(
    template=(
        "Generate the name, age, and city of a war veteran from {country}.\n"
        "{format_instructions}"
    ),
    input_variables=["country"],
    partial_variables={
        "format_instructions": parser.get_format_instructions()
    }
)

# 6️⃣ Build the chain
chain = template | model | parser

# 7️⃣ Invoke the chain
final_result = chain.invoke({"country": "India"})

# 8️⃣ Print structured output
print(final_result)