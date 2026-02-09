from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, sessionmaker
from sqlalchemy import Integer, String,TIMESTAMP, JSON, create_engine
from sqlalchemy.sql import func
import json
from dotenv import load_dotenv
import os 
from datetime import datetime
# import .env
load_dotenv()
POSTGRES_URL = os.getenv("POSTGRES_URL")
if POSTGRES_URL is None:
    raise ValueError("POSTGRES_URL environment variable is not set")


class Base(DeclarativeBase):
    pass 

class AnalysisReports(Base):
    __tablename__ = "resume_analysis_reports"
    id: Mapped[int] = mapped_column(Integer, primary_key=True, nullable=False)
    job_title: Mapped[str] = mapped_column(String(50), nullable=False)
    candidate_name: Mapped[str] = mapped_column(String(50), nullable=True)
    fit_score: Mapped[int] = mapped_column(Integer, nullable=False)
    missing_skills: Mapped[list[str]] = mapped_column(JSON, nullable=False)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP(timezone=True), server_default=func.now(), nullable=False)

engine = create_engine(POSTGRES_URL)

LocalSession = sessionmaker(bind=engine)