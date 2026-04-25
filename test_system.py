#!/usr/bin/env python3
"""
Test script to validate the AI Talent Scouting Agent
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from models.jd_parser import JDParser
from models.candidate_matcher import CandidateMatcher
from models.engagement_agent import EngagementAgent
from models.scoring_engine import ScoringEngine

def test_system():
    print("Testing AI Talent Scouting Agent...")
    
    # Sample job description
    job_description = """
    Senior Python Developer
    
    We are looking for an experienced Python developer with 5+ years of experience.
    
    Required Skills:
    - Python (Django/Flask)
    - AWS Cloud Services
    - PostgreSQL/MySQL
    - Docker & Kubernetes
    - REST API Development
    
    Location: Remote/San Francisco
    
    Responsibilities:
    - Lead development team
    - Architect scalable solutions
    - Mentor junior developers
    """
    
    try:
        # Test 1: Job Description Parsing
        print("\n1. Testing Job Description Parser...")
        jd_parser = JDParser()
        jd_data = jd_parser.parse(job_description)
        print(f"   OK Parsed title: {jd_data['title']}")
        print(f"   OK Skills found: {jd_data['skills']}")
        print(f"   OK Experience: {jd_data['experience_years']} years")
        print(f"   OK Level: {jd_data['level']}")
        
        # Test 2: Candidate Matching
        print("\n2. Testing Candidate Matcher...")
        matcher = CandidateMatcher()
        candidates = matcher.find_matches(jd_data)
        print(f"   OK Found {len(candidates)} candidates")
        print(f"   OK Top candidate: {candidates[0]['name']} (Score: {candidates[0]['match_score']:.1f})")
        
        # Test 3: Engagement Agent
        print("\n3. Testing Engagement Agent...")
        engagement_agent = EngagementAgent()
        top_candidate = candidates[0]
        engagement_result = engagement_agent.engage(top_candidate, jd_data)
        print(f"   OK Engagement response generated")
        print(f"   OK Enthusiasm level: {engagement_result.get('enthusiasm', 0):.2f}")
        
        # Test 4: Scoring Engine
        print("\n4. Testing Scoring Engine...")
        scoring_engine = ScoringEngine()
        
        # Add engagement results to candidates
        for candidate in candidates[:3]:  # Test top 3
            engagement = engagement_agent.engage(candidate, jd_data)
            candidate.update(engagement)
        
        ranked_candidates = scoring_engine.rank_candidates(candidates[:3], jd_data)
        print(f"   OK Ranked {len(ranked_candidates)} candidates")
        
        # Display results
        print("\nFinal Results:")
        print("=" * 60)
        for i, candidate in enumerate(ranked_candidates, 1):
            print(f"{i}. {candidate['name']}")
            print(f"   Combined Score: {candidate['combined_score']:.1f}")
            print(f"   Match: {candidate['match_score']:.1f} | Interest: {candidate['interest_score']:.1f}")
            print(f"   Recommendation: {candidate['recommendation']}")
            print(f"   Skills: {', '.join(candidate['skills'][:3])}...")
            print()
        
        print("OK All tests passed! System is working correctly.")
        return True
        
    except Exception as e:
        print(f"ERROR Test failed: {str(e)}")
        import traceback
        traceback.print_exc()
        return False

if __name__ == "__main__":
    success = test_system()
    sys.exit(0 if success else 1)