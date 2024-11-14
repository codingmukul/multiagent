import streamlit as st
from crewai import Crew, Process
from agents import company_researcher, case_generator, resource_collector
from tasks import research_task, use_case_task, resource_collection_task
import tempfile

# Configure Crew setup
crew = Crew(
    agents=[company_researcher, case_generator, resource_collector],
    tasks=[research_task, use_case_task, resource_collection_task],
    process=Process.sequential,
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Streamlit Interface
st.title("Company Analysis with Multiagents")
st.subheader("By Mukul Aggarwal")
st.write("Enter a company name to generate research insights, use cases, and resources.")

# Input for company name
company_name = st.text_input("Company Name")

# Check if the reports have been generated before
if 'reports_generated' not in st.session_state:
    st.session_state.reports_generated = False

# Button to start the process
if st.button("Generate Reports"):
    # Start the task execution process only if reports haven't been generated yet
    if not st.session_state.reports_generated:
        result = crew.kickoff(inputs={'company': company_name})
        
        # Save markdown outputs to temporary files and store paths in session state
        def save_md_to_file(md_content):
            with tempfile.NamedTemporaryFile(delete=False, suffix=".md") as temp_md:
                temp_md.write(md_content.encode('utf-8'))
                return temp_md.name

        # Store file paths in session state
        st.session_state.research_md = save_md_to_file(research_task.output.raw)
        st.session_state.use_case_md = save_md_to_file(use_case_task.output.raw)
        st.session_state.resource_md = save_md_to_file(resource_collection_task.output.raw)

        # Set reports_generated to True to prevent regeneration
        st.session_state.reports_generated = True

# Display download buttons only if the reports are generated
if st.session_state.reports_generated:
    # Arrange download buttons in a single row
    st.subheader("Download Reports")
    col1, col2, col3 = st.columns(3)

    with col1:
        with open(st.session_state.research_md, "rb") as file:
            st.download_button(label="Download Research Report", data=file, file_name="Research_Report.md", mime="text/markdown")
    
    with col2:
        with open(st.session_state.use_case_md, "rb") as file:
            st.download_button(label="Download Use Case Report", data=file, file_name="Use_Case_Report.md", mime="text/markdown")
    
    with col3:
        with open(st.session_state.resource_md, "rb") as file:
            st.download_button(label="Download Resource Report", data=file, file_name="Resource_Report.md", mime="text/markdown")
    
    # Display the raw markdown output in separate tabs
    st.subheader("Reports Output")

    # Create tabs for each report
    tab1, tab2, tab3 = st.tabs(["Research Report", "Use Case Report", "Resource Report"])

    with tab1:
        st.markdown(research_task.output.raw)

    with tab2:
        st.markdown(use_case_task.output.raw)

    with tab3:
        st.markdown(resource_collection_task.output.raw)
