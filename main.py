from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import uvicorn
import os
from dotenv import load_dotenv

from models.jd_parser import JDParser
from models.candidate_matcher import CandidateMatcher
from models.engagement_agent import EngagementAgent
from models.scoring_engine import ScoringEngine

load_dotenv()

app = FastAPI(title="AI Talent Scouting Agent")
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# Initialize components
jd_parser = JDParser()
candidate_matcher = CandidateMatcher()
engagement_agent = EngagementAgent()
scoring_engine = ScoringEngine()

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/process_job")
async def process_job(job_description: str = Form(...)):
    try:
        # Parse job description
        jd_data = jd_parser.parse(job_description)
        
        # Find matching candidates
        candidates = candidate_matcher.find_matches(jd_data)
        
        # Engage with candidates
        engaged_candidates = []
        for candidate in candidates:
            engagement_result = engagement_agent.engage(candidate, jd_data)
            engaged_candidates.append({**candidate, **engagement_result})
        
        # Score and rank candidates
        ranked_candidates = scoring_engine.rank_candidates(engaged_candidates, jd_data)
        
        return {
            "success": True,
            "job_requirements": jd_data,
            "candidates": ranked_candidates[:10]  # Top 10
        }
    except Exception as e:
        return {"success": False, "error": str(e)}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)