# Architecture & Technical Design

## System Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   Web Interface │    │   FastAPI Server │    │  AI Components  │
│                 │    │                  │    │                 │
│  • HTML/CSS/JS  │◄──►│  • REST API      │◄──►│  • JD Parser    │
│  • Form Input   │    │  • Request       │    │  • Matcher      │
│  • Results UI   │    │    Handling      │    │  • Engagement   │
└─────────────────┘    └──────────────────┘    │  • Scoring      │
                                               └─────────────────┘
                              │
                              ▼
                       ┌──────────────────┐
                       │   Data Layer     │
                       │                  │
                       │  • Candidates DB │
                       │  • Scoring Logic │
                       │  • ML Models     │
                       └──────────────────┘
```

## Component Details

### 1. Job Description Parser (`jd_parser.py`)
- **Purpose**: Extract structured data from unstructured job descriptions
- **Technology**: Regex patterns + NLP techniques
- **Output**: Skills, experience, level, location requirements

**Key Features:**
- Skill extraction using predefined patterns
- Experience level detection (junior/mid/senior/principal)
- Location preference parsing
- Job title normalization

### 2. Candidate Matcher (`candidate_matcher.py`)
- **Purpose**: Find and score candidate matches
- **Technology**: TF-IDF vectorization + cosine similarity
- **Scoring Components**:
  - Skills alignment (40%)
  - Experience level (30%)
  - Semantic similarity (20%)
  - Location preference (10%)

**Algorithm:**
```python
match_score = (
    skill_overlap_ratio * 0.4 +
    experience_alignment * 0.3 +
    semantic_similarity * 0.2 +
    location_match * 0.1
) * 100
```

### 3. Engagement Agent (`engagement_agent.py`)
- **Purpose**: Simulate candidate conversations and assess interest
- **Technology**: OpenAI GPT-3.5 (with fallback simulation)
- **Output**: Response text, enthusiasm level, availability, salary expectations

**Interest Scoring:**
```python
interest_score = (
    enthusiasm * 0.5 +
    availability_score * 0.3 +
    salary_alignment * 0.2
) * 100
```

### 4. Scoring Engine (`scoring_engine.py`)
- **Purpose**: Combine match and interest scores for final ranking
- **Formula**: `Combined Score = (Match Score × 0.6) + (Interest Score × 0.4)`
- **Output**: Ranked candidate list with explanations

## Data Flow

1. **Input**: Job description text
2. **Parse**: Extract requirements using NLP
3. **Match**: Find candidates using similarity algorithms
4. **Engage**: Simulate conversations with each candidate
5. **Score**: Calculate combined match + interest scores
6. **Rank**: Sort candidates by combined score
7. **Output**: Structured candidate shortlist

## Scoring Methodology

### Match Score Calculation
```
Skills Alignment = (Overlapping Skills / Required Skills) × 40
Experience Match = max(0, 1 - |candidate_exp - required_exp| / 10) × 30
Semantic Similarity = cosine_similarity(jd_vector, candidate_vector) × 20
Location Preference = location_match_bonus × 10
```

### Interest Score Calculation
```
Enthusiasm = AI_assessed_enthusiasm × 50
Availability = availability_timeline_score × 30
Salary Fit = salary_expectation_alignment × 20
```

### Final Ranking
```
Combined Score = (Match Score × 0.6) + (Interest Score × 0.4)
```

## Technology Stack

- **Backend**: FastAPI (Python)
- **AI/ML**: OpenAI GPT-3.5, scikit-learn, spaCy
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Data**: JSON file storage
- **Deployment**: Local development server

## Scalability Considerations

1. **Database**: Currently JSON files, can migrate to PostgreSQL/MongoDB
2. **Caching**: Add Redis for candidate search results
3. **AI**: Batch processing for multiple candidates
4. **API**: Rate limiting and authentication for production
5. **Search**: Elasticsearch for advanced candidate discovery

## Security & Privacy

- No sensitive data stored permanently
- API key management through environment variables
- Input validation and sanitization
- HTTPS recommended for production deployment