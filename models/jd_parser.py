import re
from typing import Dict, List

class JDParser:
    def __init__(self):
        self.skill_patterns = [
            r'\b(?:python|java|javascript|react|node\.?js|angular|vue|django|flask|spring|aws|azure|gcp|docker|kubernetes|sql|nosql|mongodb|postgresql|mysql|git|ci/cd|devops|machine learning|ai|data science|tensorflow|pytorch|scikit-learn|pandas|numpy)\b',
            r'\b(?:html|css|typescript|php|ruby|go|rust|scala|kotlin|swift|c\+\+|c#|\.net|laravel|rails|express|fastapi|graphql|rest|api|microservices|agile|scrum|jira|confluence)\b'
        ]
        
        self.experience_patterns = [
            r'(\d+)[\+\-\s]*(?:years?|yrs?)\s*(?:of\s*)?(?:experience|exp)',
            r'(?:minimum|min|at least)\s*(\d+)\s*(?:years?|yrs?)',
            r'(\d+)\s*to\s*(\d+)\s*(?:years?|yrs?)'
        ]
        
        self.level_keywords = {
            'junior': ['junior', 'entry', 'associate', '0-2 years', 'graduate'],
            'mid': ['mid', 'intermediate', '2-5 years', '3-6 years'],
            'senior': ['senior', 'lead', '5+ years', '7+ years', 'expert'],
            'principal': ['principal', 'staff', 'architect', '10+ years']
        }

    def parse(self, job_description: str) -> Dict:
        jd_lower = job_description.lower()
        
        # Extract skills
        skills = self._extract_skills(jd_lower)
        
        # Extract experience requirements
        experience = self._extract_experience(jd_lower)
        
        # Determine seniority level
        level = self._determine_level(jd_lower, experience)
        
        # Extract location preferences
        location = self._extract_location(job_description)
        
        # Extract job title
        title = self._extract_title(job_description)
        
        return {
            'title': title,
            'skills': skills,
            'experience_years': experience,
            'level': level,
            'location': location,
            'raw_description': job_description
        }
    
    def _extract_skills(self, text: str) -> List[str]:
        skills = set()
        for pattern in self.skill_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            skills.update([match.lower() for match in matches])
        return list(skills)
    
    def _extract_experience(self, text: str) -> int:
        for pattern in self.experience_patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            if matches:
                if isinstance(matches[0], tuple):
                    return int(matches[0][0])  # Take minimum from range
                return int(matches[0])
        return 0
    
    def _determine_level(self, text: str, experience: int) -> str:
        for level, keywords in self.level_keywords.items():
            if any(keyword in text for keyword in keywords):
                return level
        
        # Fallback to experience-based determination
        if experience <= 2:
            return 'junior'
        elif experience <= 5:
            return 'mid'
        elif experience <= 8:
            return 'senior'
        else:
            return 'principal'
    
    def _extract_location(self, text: str) -> str:
        location_patterns = [
            r'(?:location|based in|located in):\s*([^\n\r]+)',
            r'(?:remote|hybrid|on-site|onsite)',
            r'(?:san francisco|new york|london|berlin|toronto|sydney|mumbai|bangalore)'
        ]
        
        for pattern in location_patterns:
            match = re.search(pattern, text, re.IGNORECASE)
            if match:
                return match.group(1) if match.groups() else match.group(0)
        
        return 'Not specified'
    
    def _extract_title(self, text: str) -> str:
        lines = text.split('\n')
        for line in lines[:3]:  # Check first 3 lines
            line = line.strip()
            if line and not line.startswith(('job', 'position', 'role')):
                if any(word in line.lower() for word in ['developer', 'engineer', 'manager', 'analyst', 'scientist']):
                    return line
        return 'Software Engineer'