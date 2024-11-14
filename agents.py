from crewai import Agent, LLM
from dotenv import load_dotenv
from tools import tool
import os

# Load environment variables
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# Retrieve the GROQ API key from environment variables
GROQ_API_KEY = os.getenv("GROQ_API_KEY")

# Initialize the LLM with the specified model and API key
llm= LLM(
    model="groq/llama3-8b-8192",
    api_key=GROQ_API_KEY
)

# Company Researcher Agent
company_researcher = Agent(
    role='Company Researcher',
    goal="""Research the company {company} to understand its key offerings and strategic focus areas. Identify the industry the company operates in (e.g., Automotive, Manufacturing, Finance, Retail, Healthcare). Investigate the company’s vision, product offerings, and any strategic goals related to operations, customer experience, supply chain, innovation, or growth. Provide insights into how the company’s approach aligns with trends in the industry and its future direction. Give a brief summary of the company.""",
    verbose=True,
    memory=False,
    backstory="Expert in understanding the industry, providing the key offerings and strategic focus areas of a company",
    tools=[tool],
    llm = llm,
    allow_delegation=True
)

# Use Case Generator Agent
case_generator = Agent(
    role='Use Case Generator',
    goal="""Based on description, analyze industry trends and standards within the company’s sector related to AI, ML, and automation. Propose relevant use cases where the company can leverage GenAI, LLMs, and ML technologies to improve their processes, enhance customer satisfaction, and boost operational efficiency.""",
    verbose=True,
    memory=False,
    backstory="Expert in understanding the description, gives a description followed by 15-20 use cases",
    tools=[tool],
    llm = llm,
    allow_delegation=True
)

# Resource Collector Agent
resource_collector = Agent(
    role='Resource Asset Collection',
    goal="""Based on use_cases, search for relevant datasets on platforms like Kaggle, HuggingFace, and GitHub and provide links. Also, propose GenAI solutions like document search, automated report generation, and AI-powered chat systems for internal or customer-facing purposes.""",
    verbose=True,
    memory=False,
    backstory="Datasets link finder on GitHub, Kaggle, and HuggingFace",
    tools=[tool],
    llm = llm,
    allow_delegation=False
)
