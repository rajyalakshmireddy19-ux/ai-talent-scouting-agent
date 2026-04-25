from typing import Dict, List
from models.engagement_agent import EngagementAgent

class ScoringEngine:
    def __init__(self):
        self.engagement_agent = EngagementAgent()
        
        # Scoring weights
        self.match_weight = 0.6
        self.interest_weight = 0.4
    
    def rank_candidates(self, candidates: List[Dict], jd_data: Dict) -> List[Dict]:
        """Rank candidates based on combined match and interest scores"""
        
        ranked_candidates = []
        
        for candidate in candidates:
            # Calculate interest score from engagement
            interest_score = self.engagement_agent.calculate_interest_score(candidate)
            
            # Get match score (already calculated)
            match_score = candidate.get('match_score', 0)
            
            # Calculate combined score
            combined_score = (match_score * self.match_weight) + (interest_score * self.interest_weight)
            
            # Create explanation
            explanation = self._generate_explanation(candidate, match_score, interest_score, jd_data)
            
            ranked_candidate = {
                'id': candidate['id'],
                'name': candidate['name'],
                'email': candidate['email'],
                'current_role': candidate['current_role'],
                'location': candidate['location'],
                'skills': candidate['skills'],
                'experience_years': candidate['experience_years'],
                'match_score': round(match_score, 1),
                'interest_score': round(interest_score, 1),
                'combined_score': round(combined_score, 1),
                'engagement_response': candidate.get('response', ''),
                'availability': candidate.get('availability', 'Not specified'),
                'salary_expectation': candidate.get('salary_expectation', 0),
                'explanation': explanation,
                'recommendation': self._get_recommendation(combined_score)
            }
            
            ranked_candidates.append(ranked_candidate)
        
        # Sort by combined score
        ranked_candidates.sort(key=lambda x: x['combined_score'], reverse=True)
        
        return ranked_candidates
    
    def _generate_explanation(self, candidate: Dict, match_score: float, interest_score: float, jd_data: Dict) -> str:
        """Generate explanation for the candidate's score"""
        
        explanations = []
        
        # Match score explanation
        skill_overlap = len(set(candidate['skills']) & set(jd_data['skills']))
        total_required_skills = len(jd_data['skills'])
        
        if skill_overlap >= total_required_skills * 0.8:
            explanations.append(f"Strong technical match ({skill_overlap}/{total_required_skills} required skills)")
        elif skill_overlap >= total_required_skills * 0.5:
            explanations.append(f"Good technical fit ({skill_overlap}/{total_required_skills} required skills)")
        else:
            explanations.append(f"Partial technical match ({skill_overlap}/{total_required_skills} required skills)")
        
        # Experience explanation
        exp_diff = abs(candidate['experience_years'] - jd_data['experience_years'])
        if exp_diff <= 1:
            explanations.append("Perfect experience level match")
        elif exp_diff <= 3:
            explanations.append("Good experience level alignment")
        else:
            explanations.append("Experience level gap present")
        
        # Interest explanation
        enthusiasm = candidate.get('enthusiasm', 0.5)
        if enthusiasm > 0.8:
            explanations.append("High enthusiasm and interest")
        elif enthusiasm > 0.6:
            explanations.append("Moderate interest level")
        else:
            explanations.append("Reserved interest, may need more convincing")
        
        # Availability
        availability = candidate.get('availability', '').lower()
        if 'immediate' in availability:
            explanations.append("Immediately available")
        elif 'week' in availability:
            explanations.append("Available soon")
        else:
            explanations.append("Longer notice period required")
        
        return "; ".join(explanations)
    
    def _get_recommendation(self, combined_score: float) -> str:
        """Get hiring recommendation based on score"""
        
        if combined_score >= 80:
            return "Strong Hire - Schedule interview immediately"
        elif combined_score >= 70:
            return "Hire - Good candidate, proceed with interview"
        elif combined_score >= 60:
            return "Maybe - Consider if other candidates unavailable"
        else:
            return "Pass - Look for better matches"
    
    def get_scoring_breakdown(self) -> Dict:
        """Return scoring methodology for transparency"""
        
        return {
            "match_score_components": {
                "skills_alignment": "40%",
                "experience_level": "30%", 
                "semantic_similarity": "20%",
                "location_preference": "10%"
            },
            "interest_score_components": {
                "response_enthusiasm": "50%",
                "availability_timeline": "30%",
                "salary_expectations": "20%"
            },
            "final_score_weights": {
                "match_score": f"{self.match_weight * 100}%",
                "interest_score": f"{self.interest_weight * 100}%"
            }
        }