#!/usr/bin/env python3
"""
Demo script showcasing the AI Talent Scouting Agent capabilities
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.jd_parser import JDParser
from models.candidate_matcher import CandidateMatcher
from models.engagement_agent import EngagementAgent
from models.scoring_engine import ScoringEngine

def run_demo():
    print("=" * 70)
    print("        AI TALENT SCOUTING & ENGAGEMENT AGENT - DEMO")
    print("=" * 70)
    
    # Sample job descriptions for different scenarios
    job_descriptions = [
        {
            "name": "Senior Python Developer",
            "description": """
            Senior Python Developer - Remote/San Francisco
            
            We are seeking an experienced Python developer with 5+ years of experience
            to join our growing engineering team.
            
            Required Skills:
            - Python (Django/Flask)
            - AWS Cloud Services  
            - PostgreSQL/MySQL
            - Docker & Kubernetes
            - REST API Development
            - Team Leadership
            
            Responsibilities:
            - Lead development of scalable web applications
            - Mentor junior developers
            - Architect cloud-native solutions
            - Collaborate with product teams
            
            Location: Remote or San Francisco Bay Area
            """
        },
        {
            "name": "Data Scientist",
            "description": """
            Data Scientist - Machine Learning Focus
            
            Join our AI team to build next-generation ML models.
            
            Requirements:
            - 3+ years in data science
            - Python, TensorFlow, PyTorch
            - Statistical analysis and modeling
            - AWS/GCP experience
            - SQL and data warehousing
            
            Location: Boston or Remote
            """
        }
    ]
    
    # Initialize components
    jd_parser = JDParser()
    candidate_matcher = CandidateMatcher()
    engagement_agent = EngagementAgent()
    scoring_engine = ScoringEngine()
    
    for i, job in enumerate(job_descriptions, 1):
        print(f"\\n{i}. DEMO SCENARIO: {job['name']}")
        print("-" * 50)
        
        # Parse job description
        print("Step 1: Parsing Job Description...")
        jd_data = jd_parser.parse(job['description'])
        print(f"  Title: {jd_data['title']}")
        print(f"  Skills: {', '.join(jd_data['skills'][:5])}...")
        print(f"  Experience: {jd_data['experience_years']} years")
        print(f"  Level: {jd_data['level']}")
        
        # Find matching candidates
        print("\\nStep 2: Finding Matching Candidates...")
        candidates = candidate_matcher.find_matches(jd_data)
        print(f"  Found {len(candidates)} candidates")
        
        # Engage with top candidates
        print("\\nStep 3: AI Engagement Simulation...")
        top_candidates = candidates[:3]
        for candidate in top_candidates:
            engagement_result = engagement_agent.engage(candidate, jd_data)
            candidate.update(engagement_result)
        
        # Score and rank
        print("\\nStep 4: Scoring and Ranking...")
        ranked_candidates = scoring_engine.rank_candidates(top_candidates, jd_data)
        
        # Display results
        print("\\nRESULTS - Top 3 Candidates:")
        print("=" * 40)
        
        for j, candidate in enumerate(ranked_candidates, 1):
            print(f"{j}. {candidate['name']} - Combined Score: {candidate['combined_score']:.1f}")
            print(f"   Match: {candidate['match_score']:.1f} | Interest: {candidate['interest_score']:.1f}")
            print(f"   Role: {candidate['current_role']}")
            print(f"   Skills: {', '.join(candidate['skills'][:3])}...")
            print(f"   Response: \"{candidate.get('response', 'N/A')[:60]}...\"")
            print(f"   Recommendation: {candidate['recommendation']}")
            print()
        
        if i < len(job_descriptions):
            input("Press Enter to continue to next demo...")
    
    print("\\n" + "=" * 70)
    print("                    DEMO COMPLETE!")
    print("=" * 70)
    print("\\nTo run the full web application:")
    print("  python main.py")
    print("  Then open: http://localhost:8000")
    print("\\nFor more details, see README.md and ARCHITECTURE.md")

if __name__ == "__main__":
    run_demo()