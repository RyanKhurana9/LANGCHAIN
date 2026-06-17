from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import JsonOutputParser

# 1️ Load API key before creating model
load_dotenv()

# 2️ Initialize model (requires API key in env)
model = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash-lite"
)

# 3 Initialize JSON parser
parser = JsonOutputParser()

# 4️ Create prompt template with proper partial variable
template = PromptTemplate(
    template="Give me the name, age, and city of fictional war hero and country and how did the he got injured and which aircraft did he flew and against whom he was fighting {format_instruction}",
    input_variables=[],
    partial_variables={"format_instruction": parser.get_format_instructions()}
)
betichod=template|model|parser

prompt1 = template.format()
result=betichod.invoke()


 
output1=model.invoke(prompt1)
print(output1.content )
print(type(output1 ))
