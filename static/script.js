document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('jobForm');
    const submitBtn = document.getElementById('submitBtn');
    const btnText = submitBtn.querySelector('.btn-text');
    const loading = submitBtn.querySelector('.loading');
    const resultsSection = document.getElementById('results');
    const errorSection = document.getElementById('error');

    form.addEventListener('submit', async function(e) {
        e.preventDefault();
        
        const jobDescription = document.getElementById('jobDescription').value.trim();
        
        if (!jobDescription) {
            showError('Please enter a job description');
            return;
        }

        // Show loading state
        setLoading(true);
        hideResults();
        hideError();

        try {
            const formData = new FormData();
            formData.append('job_description', jobDescription);

            const response = await fetch('/process_job', {
                method: 'POST',
                body: formData
            });

            const data = await response.json();

            if (data.success) {
                displayResults(data);
            } else {
                showError(data.error || 'An error occurred while processing the job description');
            }
        } catch (error) {
            showError('Network error: ' + error.message);
        } finally {
            setLoading(false);
        }
    });

    function setLoading(isLoading) {
        submitBtn.disabled = isLoading;
        if (isLoading) {
            btnText.style.display = 'none';
            loading.style.display = 'inline';
        } else {
            btnText.style.display = 'inline';
            loading.style.display = 'none';
        }
    }

    function displayResults(data) {
        const { job_requirements, candidates } = data;
        
        // Display job summary
        displayJobSummary(job_requirements);
        
        // Display candidates
        displayCandidates(candidates);
        
        // Show results section
        resultsSection.style.display = 'block';
        resultsSection.scrollIntoView({ behavior: 'smooth' });
    }

    function displayJobSummary(jobData) {
        const summaryDiv = document.getElementById('jobSummary');
        
        const skillsHtml = jobData.skills.map(skill => 
            `<span class="skill-tag">${skill}</span>`
        ).join('');

        summaryDiv.innerHTML = `
            <h3>📋 Parsed Job Requirements</h3>
            <p><strong>Title:</strong> ${jobData.title}</p>
            <p><strong>Experience Required:</strong> ${jobData.experience_years} years</p>
            <p><strong>Level:</strong> ${jobData.level}</p>
            <p><strong>Location:</strong> ${jobData.location}</p>
            <div class="skills">
                <strong>Required Skills:</strong>
                ${skillsHtml}
            </div>
        `;
    }

    function displayCandidates(candidates) {
        const candidatesDiv = document.getElementById('candidatesList');
        
        if (!candidates || candidates.length === 0) {
            candidatesDiv.innerHTML = '<p>No matching candidates found.</p>';
            return;
        }

        const candidatesHtml = candidates.map((candidate, index) => {
            const skillsHtml = candidate.skills.map(skill => 
                `<span class="skill-badge">${skill}</span>`
            ).join('');

            const recommendationClass = getRecommendationClass(candidate.recommendation);
            
            return `
                <div class="candidate-card">
                    <div class="candidate-header">
                        <div class="candidate-info">
                            <h3>${index + 1}. ${candidate.name}</h3>
                            <p>${candidate.current_role} • ${candidate.location}</p>
                            <p>${candidate.email}</p>
                        </div>
                        <div class="score-display">
                            <div class="combined-score">${candidate.combined_score}</div>
                            <div class="score-breakdown">
                                Match: ${candidate.match_score} | Interest: ${candidate.interest_score}
                            </div>
                        </div>
                    </div>
                    
                    <div class="candidate-details">
                        <div class="detail-group">
                            <h4>Experience</h4>
                            <p>${candidate.experience_years} years</p>
                        </div>
                        <div class="detail-group">
                            <h4>Availability</h4>
                            <p>${candidate.availability}</p>
                        </div>
                        <div class="detail-group">
                            <h4>Salary Expectation</h4>
                            <p>$${candidate.salary_expectation ? candidate.salary_expectation.toLocaleString() : 'Not specified'}</p>
                        </div>
                        <div class="detail-group">
                            <h4>Skills</h4>
                            <div class="skills-list">
                                ${skillsHtml}
                            </div>
                        </div>
                    </div>
                    
                    ${candidate.engagement_response ? `
                        <div class="engagement-response">
                            <strong>💬 Candidate Response:</strong><br>
                            "${candidate.engagement_response}"
                        </div>
                    ` : ''}
                    
                    <div class="explanation">
                        <strong>📊 Analysis:</strong> ${candidate.explanation}
                    </div>
                    
                    <div style="text-align: right; margin-top: 15px;">
                        <span class="recommendation ${recommendationClass}">
                            ${candidate.recommendation}
                        </span>
                    </div>
                </div>
            `;
        }).join('');

        candidatesDiv.innerHTML = `
            <h3>🎯 Top Candidates (${candidates.length} found)</h3>
            ${candidatesHtml}
        `;
    }

    function getRecommendationClass(recommendation) {
        const rec = recommendation.toLowerCase();
        if (rec.includes('strong hire')) return 'strong-hire';
        if (rec.includes('hire')) return 'hire';
        if (rec.includes('maybe')) return 'maybe';
        return 'pass';
    }

    function showError(message) {
        const errorDiv = document.getElementById('errorMessage');
        errorDiv.textContent = message;
        errorSection.style.display = 'block';
        errorSection.scrollIntoView({ behavior: 'smooth' });
    }

    function hideError() {
        errorSection.style.display = 'none';
    }

    function hideResults() {
        resultsSection.style.display = 'none';
    }
});