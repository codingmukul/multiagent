# Company Analysis with Multiagents

This project is designed to analyze companies and generate insights based on their industry, strategic goals, and technology adoption. It leverages multiple AI agents and tools to research the company, propose AI/ML use cases, and collect relevant datasets and resources.

## Project Setup

### Prerequisites
Before running the application, ensure you have the following:

- Python 3.10
- `pip` for package management
- Environment variables set up for the API keys

### Install Dependencies

Clone the repository and install the required dependencies:

```bash
git clone <repository_url>
cd <project_directory>
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root directory and add the following keys:

```
EXA_API_KEY=<your_exa_api_key>
OPENAI_API_KEY=<your_open_api_key>
GROQ_API_KEY=<your_groq_api_key>
```

### Project Structure

- **`app.py`**: Main entry point that integrates the agents and tasks. Provides a Streamlit interface for user input and report generation.
- **`agents.py`**: Defines the agents responsible for company research, use case generation, and resource collection.
- **`tasks.py`**: Contains the tasks related to company research, use case generation, and resource collection.
- **`tools.py`**: Defines the tools used by the agents for internet searching and data collection.
- **`requirements.txt`**: List of required Python packages.

### How to Run

To run the application, execute the following command:

```bash
streamlit run app.py
```

This will launch the Streamlit app in your browser where you can input a company name and generate reports based on the research, use cases, and resources.

### Features

- **Company Research**: The `company_researcher` agent investigates a company's offerings, strategic goals, and industry alignment.
- **Use Case Generation**: The `case_generator` agent proposes relevant use cases for AI, ML, and GenAI technologies based on the company’s sector.
- **Resource Collection**: The `resource_collector` agent gathers datasets from Kaggle, GitHub, and HuggingFace, and suggests GenAI solutions for internal and customer-facing applications.

### Reports

Once reports are generated, they will be available for download in .md format:
1. **Research Report**: Insights into the company’s vision, offerings, and industry trends.
2. **Use Case Report**: Proposed AI/ML use cases for improving operations and customer satisfaction.
3. **Resource Report**: Dataset links and proposed GenAI solutions.

### Tools Used

- **CrewAI**: Orchestrates the multi-agent system for task execution.
- **EXASearchTool**: Tool for searching relevant datasets on Kaggle, HuggingFace, and GitHub.
- **Streamlit**: Frontend for user interaction and report generation.

---

### Notes

- Ensure the API keys are valid and added to the `.env` file.
- The system leverages the powerful LLM models and external datasets for the analysis and recommendation process.