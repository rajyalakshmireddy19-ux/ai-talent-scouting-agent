import os
import random
from typing import Dict
try:
    from openai import OpenAI
except ImportError:
    OpenAI = None

class EngagementAgent:
    def __init__(self):
        self.api_key = os.getenv('OPENAI_API_KEY')
        self.client = None
        if self.api_key and OpenAI:
            try:
                self.client = OpenAI(api_key=self.api_key)
            except Exception:
                self.client = None
        
        # Fallback responses for demo without API key
        self.fallback_responses = [
            {
                'response': "Hi! I'm very interested in this opportunity. The role aligns perfectly with my Python and AWS experience. I'm available for interviews next week and looking for a salary range of $120-140k.",
                'enthusiasm': 0.9,
                'availability': 'immediate',
                'salary_expectation': 130000
            },
            {
                'response': "Thanks for reaching out. This looks like an interesting position. I have the required Python skills and some AWS experience. I'm currently employed but open to the right opportunity. Timeline would be 4-6 weeks.",
                'enthusiasm': 0.7,
                'availability': '4-6 weeks',
                'salary_expectation': 125000
            },
            {
                'response': "Hello, I appreciate you considering me. While I have Python experience, I'm not sure about the AWS requirements. I'd need to learn more about the role. Currently happy in my position but always open to growth opportunities.",
                'enthusiasm': 0.5,
                'availability': 'flexible',
                'salary_expectation': 115000
            }
        ]
    
    def engage(self, candidate: Dict, jd_data: Dict) -> Dict:
        """Simulate engagement conversation with candidate"""
        
        if self.client:
            return self._ai_engagement(candidate, jd_data)
        else:
            return self._simulated_engagement(candidate, jd_data)
    
    def _ai_engagement(self, candidate: Dict, jd_data: Dict) -> Dict:
        """Use OpenAI to generate realistic engagement"""
        try:
            if not self.client:
                return self._simulated_engagement(candidate, jd_data)
                
            prompt = f"""
            You are simulating a candidate response to a job opportunity outreach.
            
            Candidate Profile:
            - Name: {candidate['name']}
            - Skills: {', '.join(candidate['skills'])}
            - Experience: {candidate['experience_years']} years
            - Current Role: {candidate['current_role']}
            
            Job Opportunity:
            - Title: {jd_data['title']}
            - Required Skills: {', '.join(jd_data['skills'])}
            - Experience: {jd_data['experience_years']} years
            
            Generate a realistic candidate response (2-3 sentences) and provide:
            1. Response text
            2. Enthusiasm level (0.0-1.0)
            3. Availability timeline
            4. Salary expectation (number)
            
            Format as JSON with keys: response, enthusiasm, availability, salary_expectation
            """
            
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
                temperature=0.7
            )
            
            # Parse AI response (simplified for demo)
            ai_text = response.choices[0].message.content
            return self._parse_ai_response(ai_text, candidate)
            
        except Exception as e:
            print(f"AI engagement failed: {e}")
            return self._simulated_engagement(candidate, jd_data)
    
    def _simulated_engagement(self, candidate: Dict, jd_data: Dict) -> Dict:
        """Fallback simulation based on candidate-job fit"""
        
        # Calculate engagement based on match quality
        skill_overlap = len(set(candidate['skills']) & set(jd_data['skills']))
        total_skills = len(jd_data['skills'])
        skill_match_ratio = skill_overlap / max(total_skills, 1)
        
        # Experience alignment
        exp_diff = abs(candidate['experience_years'] - jd_data['experience_years'])
        exp_alignment = max(0, 1 - exp_diff / 5)
        
        # Overall fit score
        fit_score = (skill_match_ratio + exp_alignment) / 2
        
        # Select response based on fit
        if fit_score > 0.8:
            response_idx = 0  # High interest
        elif fit_score > 0.5:
            response_idx = 1  # Moderate interest
        else:
            response_idx = 2  # Low interest
        
        base_response = self.fallback_responses[response_idx].copy()
        
        # Personalize response
        base_response['response'] = base_response['response'].replace(
            "Python and AWS", 
            f"{candidate['skills'][0]} and {candidate['skills'][1] if len(candidate['skills']) > 1 else 'related technologies'}"
        )
        
        # Add some randomness
        base_response['enthusiasm'] += random.uniform(-0.1, 0.1)
        base_response['enthusiasm'] = max(0, min(1, base_response['enthusiasm']))
        
        return base_response
    
    def _parse_ai_response(self, ai_text: str, candidate: Dict) -> Dict:
        """Parse AI response into structured format"""
        # Simplified parsing - in production, use more robust JSON parsing
        try:
            import json
            return json.loads(ai_text)
        except:
            # Fallback to simulated response
            return self._simulated_engagement(candidate, {})
    
    def calculate_interest_score(self, engagement_result: Dict) -> float:
        """Calculate interest score from engagement results"""
        enthusiasm = engagement_result.get('enthusiasm', 0.5)
        
        # Availability scoring
        availability = engagement_result.get('availability', 'flexible').lower()
        if 'immediate' in availability or 'next week' in availability:
            availability_score = 1.0
        elif 'weeks' in availability:
            availability_score = 0.7
        elif 'months' in availability:
            availability_score = 0.4
        else:
            availability_score = 0.6
        
        # Salary expectation (normalized - assuming reasonable range)
        salary = engagement_result.get('salary_expectation', 100000)
        salary_score = max(0, min(1, (150000 - salary) / 50000))  # Lower expectations = higher score
        
        # Weighted combination
        interest_score = (enthusiasm * 0.5 + availability_score * 0.3 + salary_score * 0.2) * 100
        
        return min(100, interest_score)