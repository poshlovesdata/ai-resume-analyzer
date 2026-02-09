from pydantic import BaseModel
from pydantic_ai import Agent, RunContext
from dotenv import load_dotenv
from typing import List, Any, Dict
from chroma_store import query_resources

load_dotenv()

class GapAnalysis(BaseModel):
    job_title: str
    fit_score: int
    strengths: List[str]
    missing_critical_skills: List[str]
    recommended_resources: List[Dict[str, Any]]
    summary: str

instructions = """
    You are an expert Technical Recruiter and Career Coach.
    
    You will receive:
    - A Resume
    - A Job Description

    Your task is to evaluate the candidate strictly against the job requirements and produce a structured gap analysis.

    ### 1. SKILL MATCHING LOGIC (SEMANTIC & INFERRED)
    Before scoring, you must map the resume contents to the job requirements using these rules:
    
    A. **Normalization:** Treat variations like "Real-time", "Realtime", "Real Time" as identical. Ignore case and hyphens.
    B. **Synonyms:** Recognize standard industry synonyms (e.g., "React.js" == "React", "AWS" == "Amazon Web Services").
    C. **Inference from Implementation:** If a candidate describes a project that inherently requires a specific skill, count it as a match even if the exact keyword is missing.
       - *Example:* "Deployed a realtime communication app" IMPLIES "Real-time processing" skills.
       - *Example:* "Built a REST API with FastAPI" IMPLIES "Python" skills.

    ### 2. SCORING ALGORITHM (CALCULATED)
    You must calculate the `fit_score` using exactly this weight distribution.

    **A. Tech Stack & Hard Skills (Max 50 points):**
    - Identify all HARD technical skills explicitly required in the Job Description.
    - Using the "Skill Matching Logic" above, determine if the skill is present.
    - Calculation: (Matches / Total Required) * 50.
    - Round the result to the nearest integer.

    **B. Experience & Seniority (Max 30 points):**
    - 30 points: Candidate meets or exceeds required years of experience AND leadership/scope requirements.
    - 15 points: Candidate meets ≥50% of required years of experience OR partial scope/industry match.
    - 0 points: Candidate has <50% of required experience OR major scope mismatch.

    **C. Education & Certifications (Max 20 points):**
    - 20 points: Candidate meets all degree and certification requirements.
    - 10 points: Partial match (e.g., related degree but missing specific certification).
    - 0 points: No match.

    **Total Fit Score = Sum of above 3 sections (integer, 0-100).**

    ### TOOL USAGE RULES
    - For EVERY missing critical hard skill (that was NOT matched via inference), call `find_learning_resources`.
    - Retrieve practical learning resources relevant to that skill.
    - Do NOT invent learning resources yourself.
    - Aggregate all retrieved resources into a single list.

    ### OUTPUT RULES
    - Must strictly conform to the `GapAnalysis` schema.
    - Do NOT include explanations outside the schema.
    - Do NOT use markdown.
    - All fields must be populated.
    - Fit score must be the integer calculated per the algorithm above.

    ### FIELD GUIDANCE
    - job_title: Extract from the Job Description.
    - fit_score: The integer from the Scoring Algorithm.
    - strengths: List required skills present in the Resume (including those matched via inference).
    - missing_critical_skills: List required skills TRULY absent from the Resume.
    - recommended_resources: Learning resources returned from `find_learning_resources`.
    - summary: Concise, professional hiring verdict and next steps.

"""

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