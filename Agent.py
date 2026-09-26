# from urllib3 import response
from langchain.agents import create_agent
from llm_config import create_llm
from tool_calls import web_search,get_job_recommendation,get_resume_data
import gradio as gr
tools = [web_search,get_job_recommendation,get_resume_data]

print("All libraries imported")
llm = create_llm()

SYSTEM_PROMPT = """You are an Expert Job Matcher. 
Your task is to find live jobs matching the candidate's resume.

Follow these 4 execution steps sequentially:

1. RETRIEVE RESUME: Call `get_resume_data` using simple topic keywords (e.g., query="skills", query="experience").
2. EXTRACT LOGIC: From the retrieved resume:
   - Identify candidate experience level (Fresher: 0-1 yrs | Junior: 1-3 yrs | Mid: 3-5 yrs).
   - Pick 1 or 2 core tech keywords (e.g., "python", "fastapi").
   - Set a realistic minimum annual salary in INR (e.g., 500000).
3. SEARCH JOBS: Call `get_job_recommendation(what=..., salary_min=...)` using your extracted parameters.
4. FORMAT OUTPUT: Present top 3-5 live job results returned by the search tool.

Formatting Rules:
- Display: Job Title, Company, Location, Salary (in ₹ INR), Brief Description, and Apply Link (redirect_url).
- Base recommendations ONLY on live job API results. Never list past companies from the user's resume as new openings.
- If a field is missing in the result, write "Not specified".
"""

job_search_agent = create_agent(
    model = llm, 
    tools = tools,
    system_prompt= SYSTEM_PROMPT
)


def run_agent():
    response = job_search_agent.invoke(
        {"messages":
        [{"role":"user",
        "content":"Find me the best jobs based on my resume data"}]}
    )
    print("\n\n\nACTUAL RESPONSE WITH TOOLS\n\n\n",response)
    return response["messages"][-1].content
import gradio as gr 
def deploy_agent():
    with gr.Blocks(title="Career Match Agent") as iface:
        gr.Markdown("## Career Match Agent")
        gr.Markdown("""Finds job openings matches to your resume,
        using live listings and your indexed resume data""")
        find_jobs_button = gr.Button("Find Jobs",variant ="primary")
        output = gr.Textbox(label="Recommend Jobs",lines=20)
        find_jobs_button.click(fn=run_agent,inputs=None,outputs=output)
    iface.launch()

if __name__ == "__main__":
    # response = run_agent()
    # print("\nCLEAN RESPONSE\n")
    # print(response)

   deploy_agent()