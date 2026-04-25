# Git Repository Setup Script for PowerShell

Write-Host "=== AI TALENT SCOUTING AGENT - GIT SETUP ===" -ForegroundColor Green
Write-Host ""

Write-Host "Step 1: Initialize Git repository" -ForegroundColor Yellow
git init

Write-Host ""
Write-Host "Step 2: Add all files" -ForegroundColor Yellow
git add .

Write-Host ""
Write-Host "Step 3: Create initial commit" -ForegroundColor Yellow
git commit -m "Initial commit: AI-Powered Talent Scouting & Engagement Agent

- Complete working system with web UI
- JD Parser, Candidate Matcher, AI Engagement, Scoring Engine
- Dual scoring system (Match + Interest)
- Professional web interface
- Comprehensive documentation
- Built for Catalyst Hackathon"

Write-Host ""
Write-Host "Step 4: Set main branch" -ForegroundColor Yellow
git branch -M main

Write-Host ""
Write-Host "=== NEXT STEPS ===" -ForegroundColor Green
Write-Host "1. Go to https://github.com"
Write-Host "2. Click 'New Repository'"
Write-Host "3. Repository name: ai-talent-scouting-agent"
Write-Host "4. Description: AI-Powered Talent Scouting & Engagement Agent for Catalyst"
Write-Host "5. Make it PUBLIC"
Write-Host "6. DO NOT initialize with README (we have our own)"
Write-Host "7. Click 'Create Repository'"
Write-Host ""
Write-Host "8. Copy the repository URL (will be like: https://github.com/YOUR_USERNAME/ai-talent-scouting-agent.git)"
Write-Host "9. Run these commands:"
Write-Host "   git remote add origin https://github.com/YOUR_USERNAME/ai-talent-scouting-agent.git"
Write-Host "   git push -u origin main"
Write-Host ""
Write-Host "Repository will be ready!" -ForegroundColor Green