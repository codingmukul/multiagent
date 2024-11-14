from crewai import Task
from tools import tool
from agents import company_researcher, case_generator, resource_collector 

research_task = Task(
  description=(
    "Research the company {company} to understand its key offerings and strategic focus areas. Identify the industry the company operates in (e.g., Automotive, Manufacturing, Finance, Retail, Healthcare). Investigate the company’s vision, product offerings, and any strategic goals related to operations, customer experience, supply chain, innovation, or growth. Provide insights into how the company’s approach aligns with trends in the industry and its future direction. Give a brief summary of the company."
  ),
  expected_output='A brief of the company along with the list of url links of information sources.',
  tools=[tool],
  agent=company_researcher,
  # output_file='1.md'  
)

# Task for Use Case Generator Agent
use_case_task = Task(
    description=(
        "Analyze industry trends and standards in the company's sector based on description. Propose 15-20 relevant use cases where the company can leverage GenAI, LLMs, and ML technologies to improve processes, enhance customer satisfaction, and boost operational efficiency."
    ),
    expected_output='A description of industry trends and standards within the company’s sector related to AI, ML, and automation with a list of 15 to 20 use cases for applying AI/ML and GenAI technologies in the company’s processes, along with 3-4 points of descriptions for each.',
    tools=[tool],
    agent=case_generator,
    # output_file='2.md'
)

# Task for Resource Collector Agent
resource_collection_task = Task(
    description=(
        "Based on the provided use cases, search for relevant datasets on Kaggle, HuggingFace, and GitHub. Provide dataset links, and propose GenAI solutions like document search, automated report generation, and AI-powered chat systems for internal or customer-facing purposes."
    ),
    expected_output='A list of dataset links with a brief description of each dataset and proposed GenAI solutions for enhancing company operations.',
    tools=[tool],
    agent=resource_collector,
    # output_file='3.md'
)  
