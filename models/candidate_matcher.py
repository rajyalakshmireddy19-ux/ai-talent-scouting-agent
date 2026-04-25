import json
import os
from typing import Dict, List
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class CandidateMatcher:
    def __init__(self):
        self.candidates = self._load_candidates()
        self.vectorizer = TfidfVectorizer(stop_words='english', max_features=1000)
        self._prepare_candidate_vectors()
    
    def _load_candidates(self) -> List[Dict]:
        candidates_file = os.path.join('data', 'candidates.json')
        if os.path.exists(candidates_file):
            with open(candidates_file, 'r') as f:
                return json.load(f)
        return self._generate_sample_candidates()
    
    def _generate_sample_candidates(self) -> List[Dict]:
        # Generate sample candidates for demo
        sample_candidates = [
            {
                "id": 1,
                "name": "John Doe",
                "email": "john.doe@email.com",
                "skills": ["python", "django", "aws", "postgresql", "docker"],
                "experience_years": 6,
                "current_role": "Senior Python Developer",
                "location": "San Francisco",
                "summary": "Experienced Python developer with expertise in Django and cloud technologies"
            },
            {
                "id": 2,
                "name": "Jane Smith",
                "email": "jane.smith@email.com",
                "skills": ["python", "flask", "react", "mongodb", "kubernetes"],
                "experience_years": 4,
                "current_role": "Full Stack Developer",
                "location": "Remote",
                "summary": "Full-stack developer specializing in Python backend and React frontend"
            },
            {
                "id": 3,
                "name": "Mike Johnson",
                "email": "mike.johnson@email.com",
                "skills": ["java", "spring", "aws", "mysql", "microservices"],
                "experience_years": 8,
                "current_role": "Lead Java Developer",
                "location": "New York",
                "summary": "Senior Java developer with strong background in microservices architecture"
            },
            {
                "id": 4,
                "name": "Sarah Wilson",
                "email": "sarah.wilson@email.com",
                "skills": ["python", "machine learning", "tensorflow", "pandas", "aws"],
                "experience_years": 5,
                "current_role": "Data Scientist",
                "location": "Boston",
                "summary": "Data scientist with strong Python and ML engineering skills"
            },
            {
                "id": 5,
                "name": "Alex Chen",
                "email": "alex.chen@email.com",
                "skills": ["javascript", "node.js", "react", "mongodb", "docker"],
                "experience_years": 3,
                "current_role": "Frontend Developer",
                "location": "Seattle",
                "summary": "Frontend specialist with full-stack JavaScript capabilities"
            }
        ]
        
        # Save sample candidates
        os.makedirs('data', exist_ok=True)
        with open('data/candidates.json', 'w') as f:
            json.dump(sample_candidates, f, indent=2)
        
        return sample_candidates
    
    def _prepare_candidate_vectors(self):
        # Create text representations of candidates
        candidate_texts = []
        for candidate in self.candidates:
            text = f"{candidate['current_role']} {' '.join(candidate['skills'])} {candidate['summary']}"
            candidate_texts.append(text)
        
        if candidate_texts:
            self.candidate_vectors = self.vectorizer.fit_transform(candidate_texts)
    
    def find_matches(self, jd_data: Dict) -> List[Dict]:
        # Create job description vector
        jd_text = f"{jd_data['title']} {' '.join(jd_data['skills'])}"
        jd_vector = self.vectorizer.transform([jd_text])
        
        # Calculate similarities
        similarities = cosine_similarity(jd_vector, self.candidate_vectors)[0]
        
        # Score candidates
        scored_candidates = []
        for i, candidate in enumerate(self.candidates):
            match_score = self._calculate_match_score(candidate, jd_data, similarities[i])
            scored_candidates.append({
                **candidate,
                'match_score': match_score,
                'similarity': float(similarities[i])
            })
        
        # Sort by match score
        scored_candidates.sort(key=lambda x: x['match_score'], reverse=True)
        return scored_candidates
    
    def _calculate_match_score(self, candidate: Dict, jd_data: Dict, similarity: float) -> float:
        score = 0
        
        # Skills alignment (40% weight)
        skill_match = len(set(candidate['skills']) & set(jd_data['skills'])) / max(len(jd_data['skills']), 1)
        score += skill_match * 40
        
        # Experience level (30% weight)
        exp_diff = abs(candidate['experience_years'] - jd_data['experience_years'])
        exp_score = max(0, 1 - exp_diff / 10) * 30
        score += exp_score
        
        # Semantic similarity (20% weight)
        score += similarity * 20
        
        # Location preference (10% weight)
        location_score = 10 if 'remote' in jd_data['location'].lower() or candidate['location'].lower() in jd_data['location'].lower() else 5
        score += location_score
        
        return min(100, score)