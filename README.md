# 🎯 AI-Powered Talent Scouting & Engagement Agent

> **Catalyst Hackathon Submission** - An intelligent recruitment assistant that automates candidate discovery, engagement, and ranking.

[![Demo](https://img.shields.io/badge/Demo-Live-green)](http://localhost:8000)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-teal)](https://fastapi.tiangolo.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-orange)](https://openai.com)

- **Smart JD Parsing**: Extracts skills, experience, and requirements from job descriptions
- **Candidate Discovery**: Finds matching profiles with explainable scoring
- **AI Engagement**: Simulates conversational outreach to assess interest
- **Dual Scoring**: Match Score (technical fit) + Interest Score (engagement level)
- **Ranked Output**: Ready-to-use shortlist for recruiters

## 🏗️ Architecture

```
Job Description → Parser → Candidate Discovery → AI Engagement → Ranking Engine → Shortlist
```

### Components:
1. **JD Parser**: NLP-based extraction of requirements
2. **Matching Engine**: Semantic similarity + rule-based scoring
3. **Engagement Agent**: LLM-powered conversation simulation
4. **Scoring System**: Weighted combination of match and interest metrics

## 🛠️ Tech Stack

- **Backend**: Python, FastAPI
- **AI/ML**: OpenAI GPT, spaCy, sentence-transformers
- **Frontend**: HTML, CSS, JavaScript
- **Data**: JSON-based candidate database
- **Deployment**: Local development server

## 📦 Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd HR_AI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Set up environment variables:
```bash
# Create .env file
OPENAI_API_KEY=your_openai_api_key_here
```

4. Run the application:
```bash
python main.py
```

5. Open browser to `http://localhost:8000`

## 🎯 Usage

1. **Input Job Description**: Paste or type the job requirements
2. **Discover Candidates**: System finds and scores matching profiles
3. **AI Engagement**: Automated conversation simulation
4. **Review Results**: Get ranked shortlist with explanations

## 📊 Scoring Logic

### Match Score (0-100):
- Skills alignment: 40%
- Experience level: 30%
- Industry background: 20%
- Location preference: 10%

### Interest Score (0-100):
- Response enthusiasm: 50%
- Availability timeline: 30%
- Salary expectations: 20%

### Final Ranking:
`Combined Score = (Match Score × 0.6) + (Interest Score × 0.4)`

## 📁 Project Structure

```
HR_AI/
├── main.py              # FastAPI application
├── models/
│   ├── jd_parser.py     # Job description parsing
│   ├── candidate_matcher.py # Candidate discovery & matching
│   ├── engagement_agent.py  # AI conversation simulation
│   └── scoring_engine.py    # Ranking and scoring logic
├── data/
│   └── candidates.json  # Sample candidate database
├── static/
│   ├── style.css       # Frontend styling
│   └── script.js       # Frontend logic
├── templates/
│   └── index.html      # Main interface
└── requirements.txt    # Dependencies
```

## 🎬 Demo Video

[Link to demo video - 3-5 minutes walkthrough]

## 📈 Sample Input/Output

### Input:
```
Job Title: Senior Python Developer
Requirements: 5+ years Python, Django/Flask, AWS, team leadership
Location: Remote/San Francisco
```

### Output:
```
Ranked Shortlist:
1. John Doe - Combined Score: 87 (Match: 92, Interest: 78)
2. Jane Smith - Combined Score: 84 (Match: 88, Interest: 76)
3. Mike Johnson - Combined Score: 81 (Match: 85, Interest: 74)
```

## 🔧 Configuration

- Adjust scoring weights in `models/scoring_engine.py`
- Modify engagement prompts in `models/engagement_agent.py`
- Update candidate database in `data/candidates.json`

## 📝 License

MIT License - see LICENSE file for details.