from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from dotenv import load_dotenv
from typing import List, Any, Dict
from pprint import pprint
from chroma_store import query_resources

load_dotenv()

class GapAnalysis(BaseModel):
    job_title: str
    fit_score: int
    strengths: List[str]
    missing_critical_skills: List[str]
    recommended_resources: List[Dict[str, Any]]
    summary: str
    
# class LearningResources(BaseModel):
#     skill: str
#     title: str
#     provider: str
#     level: str
#     url: str
#     estimated_hours: int
#     prerequisites: List[str]

instructions = """
    You are an expert Technical Recruiter and Career Coach.
    
    You will receive:
    - A Resume
    - A Job Description

    Your task is to evaluate the candidate strictly against the job requirements and produce a structured gap analysis.

    ### SCORING ALGORITHM (STRICT AND DETERMINISTIC)
    You must calculate the `fit_score` using exactly this weight distribution. Do not estimate; calculate.

    1. **Tech Stack & Hard Skills (Max 50 points):**
    - Identify all HARD technical skills explicitly required in the Job Description.
    - A skill is considered matched if the exact term or a standard recognized synonym appears in the Resume.
    - Count how many required skills are present in the Resume.
    - Calculation: (Matches / Total Required) * 50.
    - Round the result to the nearest integer.

    2. **Experience & Seniority (Max 30 points):**
    - 30 points: Candidate meets or exceeds required years of experience AND leadership/scope requirements.
    - 15 points: Candidate meets ≥50% of required years of experience OR partial scope/industry match.
    - 0 points: Candidate has <50% of required experience OR major scope mismatch.

    3. **Education & Certifications (Max 20 points):**
    - 20 points: Candidate meets all degree and certification requirements.
    - 10 points: Partial match (e.g., related degree but missing specific certification).
    - 0 points: No match.

    **Total Fit Score = Sum of above 3 sections (integer, 0–100).**

    ### TOOL USAGE RULES
    - For EVERY missing critical hard skill, call `find_learning_resources`.
    - Retrieve practical learning resources relevant to that skill.
    - Do NOT invent learning resources yourself.
    - Aggregate all retrieved resources into a single list, **in the order the missing skills appear in the Job Description**.

    ### OUTPUT RULES
    - Must strictly conform to the `GapAnalysis` schema.
    - Do NOT include explanations outside the schema.
    - Do NOT use markdown.
    - All fields must be populated.
    - Fit score must be the integer calculated per the algorithm above.

    ### FIELD GUIDANCE
    - job_title: Extract from the Job Description.
    - fit_score: The integer from the Scoring Algorithm.
    - strengths: List required skills present in the Resume and other experience that clearly matches the role.
    - missing_criteria_skills: List required skills absent from the Resume.
    - recommended_resources: Learning resources returned from `find_learning_resources`.
    - summary: Concise, professional hiring verdict and next steps.


"""

# user_prompt = """
#     JOB TITLE: Data Engineer

# COMPANY: Fintech Solutions Ltd
# LOCATION: Remote (Nigeria)

# JOB SUMMARY
# We are looking for a Data Engineer to design, build, and maintain scalable data pipelines.
# The ideal candidate will work closely with analysts and data scientists to ensure reliable
# and well-modeled data for analytics and machine learning use cases.

# RESPONSIBILITIES
# - Design and build ETL/ELT data pipelines
# - Develop and maintain data warehouses and data marts
# - Work with large datasets from multiple data sources (APIs, databases, files)
# - Ensure data quality, validation, and monitoring
# - Optimize SQL queries and data models for performance
# - Collaborate with analysts to support reporting and dashboarding needs
# - Automate data workflows and scheduling

# REQUIRED SKILLS
# - Strong Python programming
# - Advanced SQL (CTEs, window functions, optimization)
# - Experience with ETL/ELT tools (Airflow, dbt, or similar)
# - Data warehousing concepts (star schema, fact & dimension tables)
# - Experience with PostgreSQL or other relational databases
# - Version control with Git
# - Experience working with APIs and JSON data

# PREFERRED SKILLS
# - Cloud platforms (AWS, GCP, or Azure)
# - Docker and containerization
# - Basic knowledge of data orchestration and monitoring
# - Familiarity with BI tools (Power BI, Tableau, Looker)

# EDUCATION
# - Bachelor’s degree in Computer Science, Engineering, or related field

# NICE TO HAVE
# - Experience in fintech or financial data
# - Knowledge of data security and access control


# NAME: John Doe
# ROLE: Junior Data Analyst
# LOCATION: Lagos, Nigeria
# EMAIL: johndoe@email.com
# PHONE: +234 800 000 0000

# SUMMARY
# Detail-oriented Junior Data Analyst with experience in data cleaning, analysis, and visualization.
# Comfortable working with Python and SQL to generate insights from business data.

# SKILLS
# - Python
# - SQL
# - Microsoft Excel
# - Data Cleaning
# - Data Visualization
# - Pandas
# - NumPy
# - Power BI
# - Basic Statistics

# EXPERIENCE
# Data Analyst Intern
# ABC Retail Company — Lagos, Nigeria
# Jan 2023 – Jun 2023

# - Cleaned and analyzed sales data using Python and Excel
# - Wrote SQL queries to extract data from relational databases
# - Created basic dashboards in Power BI for weekly sales reporting
# - Assisted senior analysts in ad-hoc data analysis tasks

# PROJECTS
# Sales Performance Analysis
# - Analyzed 2 years of sales data using Python
# - Identified top-performing products and seasonal trends
# - Presented findings using Power BI dashboards

# EDUCATION
# B.Sc. Computer Science
# University of Lagos
# 2019 – 2023

# CERTIFICATIONS
# - Google Data Analytics Certificate (Coursera)

# TOOLS
# - Python
# - SQL
# - Excel
# - Power BI
# - Git

#     """

resume_agent = Agent(model="openai:gpt-4o", output_type=GapAnalysis, system_prompt=instructions)


@resume_agent.tool
def find_learning_resources(ctx: RunContext, gap_keyword: str) -> List[Dict[str, Any]]:
    """
    Finds books, courses, or articles for a specific missing skill.
    Returns a list of resource objects (Title, URL, Provider).
    """
    print(f"\nAgent is searching for resources on: '{gap_keyword}'")
    
    resources = query_resources(gap_keyword, n_number=1)
    if not resources:
        return [{"title": "No specific resource found", "url": "#"}]
    return resources
   
async def run_analysis(user_prompt):
    print("Analysing Resume") 
    result = await resume_agent.run(user_prompt=user_prompt)
    
    print("\nAnalysis Complete!")
    print(f"Fit Score: {result.output.fit_score}")
    print(f"Summary: {result.output.summary}")
    print("\nRecommended Resources:")
    for res in result.output.recommended_resources:
        print(f"- {res.get('title')} ({res.get('url')})")
    return result.output
    
if __name__ == "__main__":
    # run_analysis("hello")
    pass