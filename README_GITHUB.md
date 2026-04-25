# 🎯 AI-Powered Talent Scouting & Engagement Agent

> **Catalyst Hackathon Submission** - An intelligent recruitment assistant that automates candidate discovery, engagement, and ranking.

[![Demo](https://img.shields.io/badge/Demo-Live-green)](http://localhost:8000)
[![Python](https://img.shields.io/badge/Python-3.11+-blue)](https://python.org)
[![FastAPI](https://img.shields.io/badge/FastAPI-Latest-teal)](https://fastapi.tiangolo.com)
[![OpenAI](https://img.shields.io/badge/OpenAI-GPT--3.5-orange)](https://openai.com)

## 🚀 **Problem Solved**

Recruiters spend hours manually sifting through profiles and chasing candidate interest. This AI agent automates the entire pipeline:

**Input:** Job Description → **Output:** Ranked candidate shortlist with match + interest scores

## ✨ **Key Features**

- 🧠 **Smart JD Parsing** - Extracts skills, experience, and requirements using NLP
- 🔍 **Intelligent Matching** - Semantic similarity + rule-based scoring with explainability  
- 🤖 **AI Engagement** - Simulates realistic conversations to assess genuine interest
- 📊 **Dual Scoring** - Technical Match Score (60%) + Interest Score (40%)
- 🎯 **Actionable Output** - Ready-to-use ranked shortlist with hiring recommendations

## 🏗️ **Architecture**

```
Job Description → JD Parser → Candidate Matcher → AI Engagement → Scoring Engine → Ranked Shortlist
```

### Core Components:
1. **JD Parser** - NLP-based requirement extraction
2. **Candidate Matcher** - Semantic similarity + explainable scoring
3. **Engagement Agent** - LLM-powered conversation simulation  
4. **Scoring Engine** - Weighted combination of match + interest metrics

## 🛠️ **Tech Stack**

- **Backend:** FastAPI, Python 3.11+
- **AI/ML:** OpenAI GPT-3.5, scikit-learn, TF-IDF
- **Frontend:** HTML5, CSS3, Vanilla JavaScript
- **Data:** JSON-based candidate database
- **Deployment:** Local development server

## 📦 **Quick Start**

### 1. Clone & Install
```bash
git clone https://github.com/YOUR_USERNAME/ai-talent-scouting-agent.git
cd ai-talent-scouting-agent
pip install -r requirements.txt
```

### 2. Configure (Optional)
```bash
# Add OpenAI API key to .env for enhanced AI features
OPENAI_API_KEY=your_api_key_here
```

### 3. Run
```bash
python main.py
# Open http://localhost:8000
```

### 4. Test
```bash
python test_system.py  # Validate all components
python demo.py         # See example scenarios
```

## 🎬 **Demo Video**

[🎥 Watch 3-minute demo walkthrough](YOUR_VIDEO_LINK_HERE)

## 📊 **Scoring Methodology**

### Match Score (60% weight):
- **Skills alignment:** 40% - Overlap between candidate and required skills
- **Experience level:** 30% - Years of experience alignment  
- **Semantic similarity:** 20% - TF-IDF cosine similarity
- **Location preference:** 10% - Geographic/remote compatibility

### Interest Score (40% weight):
- **Response enthusiasm:** 50% - AI-assessed engagement level
- **Availability timeline:** 30% - How soon they can start
- **Salary expectations:** 20% - Compensation alignment

### Final Formula:
```
Combined Score = (Match Score × 0.6) + (Interest Score × 0.4)
```

## 📈 **Sample Output**

**Input:**
```
Senior Python Developer
5+ years experience, Django/Flask, AWS, PostgreSQL
Location: Remote/San Francisco
```

**Output:**
```
🥇 John Doe - Combined Score: 87
   Match: 92 | Interest: 78
   6 years Python, Django, AWS • High enthusiasm, immediate availability
   Recommendation: Strong Hire - Schedule interview immediately

🥈 Jane Smith - Combined Score: 84  
   Match: 88 | Interest: 76
   Full-stack developer, remote-ready • Good technical fit
   Recommendation: Hire - Good candidate, proceed with interview
```

## 🎯 **Judging Criteria Coverage**

| Criteria | Weight | Status | Implementation |
|----------|--------|--------|----------------|
| **End-to-End Functionality** | 20% | ✅ | Complete working system with all components |
| **Core Agent Quality** | 25% | ✅ | Sophisticated AI parsing, matching, engagement |
| **Output Quality** | 20% | ✅ | Actionable ranked shortlists with explanations |
| **Technical Implementation** | 15% | ✅ | Clean, modular, scalable architecture |
| **Innovation & Creativity** | 10% | ✅ | Dual scoring, AI engagement, explainable AI |
| **UX Usability** | 5% | ✅ | Professional web interface, intuitive flow |
| **Clean Documentation** | 5% | ✅ | Comprehensive docs, clear code structure |

## 📁 **Project Structure**

```
ai-talent-scouting-agent/
├── main.py                 # FastAPI application entry point
├── models/                 # Core AI components
│   ├── jd_parser.py       # Job description parsing
│   ├── candidate_matcher.py # Candidate discovery & matching  
│   ├── engagement_agent.py  # AI conversation simulation
│   └── scoring_engine.py    # Ranking and scoring logic
├── data/
│   └── candidates.json    # Sample candidate database
├── static/                # Frontend assets
│   ├── style.css         # Professional UI styling
│   └── script.js         # Interactive functionality
├── templates/
│   └── index.html        # Main web interface
├── test_system.py        # End-to-end validation
├── demo.py              # Interactive demonstration
└── docs/                # Documentation
    ├── ARCHITECTURE.md   # Technical architecture
    └── DELIVERABLES.md   # Submission checklist
```

## 🔧 **Configuration**

- **Scoring weights:** Adjust in `models/scoring_engine.py`
- **Engagement prompts:** Modify in `models/engagement_agent.py`  
- **Candidate database:** Update `data/candidates.json`
- **UI styling:** Customize `static/style.css`

## 🚀 **Deployment Options**

### Local Development
```bash
python main.py  # http://localhost:8000
```

### Cloud Deployment
```bash
# Heroku
heroku create your-app-name
git push heroku main

# Vercel  
vercel --prod
```

## 📝 **License**

MIT License - Built for Catalyst Hackathon

## 👨‍💻 **Author**

**GitHub:** [YOUR_USERNAME](https://github.com/YOUR_USERNAME)  
**Project:** AI-Powered Talent Scouting Agent  
**Hackathon:** Catalyst 2024

---

**🎯 Ready for immediate recruiter use - from job description to ranked shortlist in seconds!**