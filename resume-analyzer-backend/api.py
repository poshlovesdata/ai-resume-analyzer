from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Any, Dict
from agent import run_analysis, GapAnalysis
from database import LocalSession, AnalysisReports
from datetime import datetime



app = FastAPI(title='Resume Analyzer')

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ResumeAndJD(BaseModel):
    job_description: str
    resume: str


@app.post("/analyse_resume", response_model=GapAnalysis)
async def analyse_resume(request: ResumeAndJD):
    """
    Analyzes a resume against a job description, finds gaps, 
    recommends resources, and saves the report to the DB.
    """
    try:
        result = await run_analysis(user_prompt=[request.job_description,request.resume])
        
        session = LocalSession()
        try:
            new_report = AnalysisReports(
                job_title=result.job_title,
                fit_score=result.fit_score,
                missing_skills=result.missing_critical_skills,
                created_at=datetime.now()
            )
            session.add(new_report)
            session.commit()
            session.refresh(new_report)
            print(f"Report saved to DB with ID: {new_report.id}")
        except Exception as db_err:
            print(f"Database Error: {db_err}")
            session.rollback()
        finally:
            session.close()
            
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
