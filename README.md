# Resume Gap Analyzer

An AI-powered application that analyzes resumes against job descriptions, identifies skill gaps, calculates a fit score, and recommends personalized learning resources to bridge the gap.

![Python](https://img.shields.io/badge/Python-3.11+-blue.svg)
![FastAPI](https://img.shields.io/badge/FastAPI-0.128+-green.svg)
![React](https://img.shields.io/badge/React-19-blue.svg)

## Features

- **AI-Powered Analysis**: Uses GPT-4o to perform intelligent resume evaluation against job requirements
- **Deterministic Scoring Algorithm**: Calculates fit scores (0-100) based on:
  - Tech Stack & Hard Skills (50 points)
  - Experience & Seniority (30 points)
  - Education & Certifications (20 points)
- **Skill Gap Identification**: Pinpoints critical missing skills required for the role
- **Personalized Learning Paths**: Automatically recommends courses, tutorials, and resources for each missing skill
- **Vector-Based Resource Search**: Uses ChromaDB to semantically match learning resources to skill gaps
- **Report Persistence**: Saves analysis reports to PostgreSQL for future reference
- **Modern UI**: Clean, responsive React frontend with real-time analysis feedback

## Architecture

![Architecture Diagram](./image.png)

## Tech Stack

### Backend

- **Python 3.11+**
- **FastAPI** - High-performance async web framework
- **pydantic-ai** - AI agent framework with structured outputs
- **OpenAI GPT-4o** - Large language model for analysis
- **ChromaDB** - Vector database for semantic resource search
- **SQLAlchemy** - ORM for PostgreSQL
- **PostgreSQL** - Database for storing analysis reports

### Frontend

- **React 19** - UI library
- **Vite** - Build tool and dev server
- **Tailwind CSS 4** - Utility-first CSS framework
- **Axios** - HTTP client
- **Lucide React** - Icon library

## Prerequisites

- Python 3.11 or higher
- Node.js 18+ and npm
- PostgreSQL database
- OpenAI API key

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/resume_gap_analyzer.git
cd resume_gap_analyzer
```

### 2. Backend Setup

```bash
# Create and activate virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=your_openai_api_key_here
POSTGRES_URL=postgresql://username:password@localhost:5432/resume_analyzer
```

### 4. Database Setup

Create the PostgreSQL database and tables:

```bash
# Connect to PostgreSQL and create database
psql -U postgres
CREATE DATABASE resume_analyzer;
\q

# The tables will be created automatically when the application starts
```

### 5. Frontend Setup

```bash
cd resume-analyzer-frontend
npm install
```

## Running the Application

### Start the Backend Server

```bash
# From the root directory
uvicorn api:app --reload --host 0.0.0.0 --port 8000
```

The API will be available at `http://localhost:8000`

### Start the Frontend Development Server

```bash
# From the resume-analyzer-frontend directory
npm run dev
```

The frontend will be available at `http://localhost:5173`

## API Documentation

Once the backend is running, access the interactive API docs at:

- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

### Endpoints

#### POST `/analyse_resume`

Analyzes a resume against a job description.

**Request Body:**

```json
{
  "job_description": "Full job description text...",
  "resume": "Candidate resume text..."
}
```

**Response:**

```json
{
  "job_title": "Data Engineer",
  "fit_score": 65,
  "strengths": ["Python", "SQL", "Power BI"],
  "missing_critical_skills": ["Apache Airflow", "dbt", "Docker"],
  "recommended_resources": [
    {
      "title": "Apache Airflow Core Concepts",
      "url": "https://airflow.apache.org/docs/...",
      "level": "Beginner",
      "provider": "Apache Software Foundation",
      "estimated_hours": 2
    }
  ],
  "summary": "The candidate shows potential but lacks key data engineering skills..."
}
```

## Scoring Algorithm

The fit score is calculated using a deterministic algorithm:

| Category                   | Max Points | Criteria                                 |
| -------------------------- | ---------- | ---------------------------------------- |
| Tech Stack & Hard Skills   | 50         | (Matched Skills / Required Skills) × 50  |
| Experience & Seniority     | 30         | Full match: 30, Partial: 15, No match: 0 |
| Education & Certifications | 20         | Full match: 20, Partial: 10, No match: 0 |

**Total Score = Sum of all categories (0-100)**

## Learning Resources Database

The application uses a curated knowledge base (`resources.json`) containing learning resources for various technical skills:

- Apache Airflow
- dbt (data build tool)
- Advanced SQL
- Python
- Docker
- Cloud Platforms (AWS, GCP, Azure)
- And more...

Resources are indexed in ChromaDB for semantic search, ensuring relevant recommendations for each skill gap.

## Project Structure

```
resume_gap_analyzer/
├── api.py                  # FastAPI application and endpoints
├── agent.py                # AI agent with GPT-4o integration
├── database.py             # SQLAlchemy models and database config
├── chroma_store.py         # ChromaDB vector store for resources
├── resources.json          # Curated learning resources database
├── requirements.txt        # Python dependencies
├── .env                    # Environment variables (not in repo)
├── chroma_db/              # ChromaDB persistent storage
└── resume-analyzer-frontend/
    ├── src/
    │   ├── App.jsx         # Main application component
    │   ├── components/
    │   │   ├── AnalysisForm.jsx    # Input form component
    │   │   ├── ScoreCard.jsx       # Score visualization
    │   │   ├── ResultSection.jsx   # Results display
    │   │   ├── LearningPath.jsx    # Resources display
    │   │   └── Navbar.jsx          # Navigation bar
    │   ├── main.jsx        # React entry point
    │   └── index.css       # Global styles
    ├── package.json        # Node.js dependencies
    └── vite.config.js      # Vite configuration
```

## Configuration

### Frontend Environment Variables

Create a `.env` file in `resume-analyzer-frontend/`:

```env
VITE_API_URL=http://localhost:8000
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [OpenAI](https://openai.com/) for GPT-4o
- [pydantic-ai](https://github.com/pydantic/pydantic-ai) for the AI agent framework
- [ChromaDB](https://www.trychroma.com/) for vector storage
- [FastAPI](https://fastapi.tiangolo.com/) for the excellent web framework

---

Built with precision for career growth.
