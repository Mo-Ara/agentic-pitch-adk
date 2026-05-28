# 🏆 Google Agentic AI Hackathon (1st Place Winner) - Open-Source Architecture Showcase

**Project Tagline:** A production-ready blueprint of an autonomous multimodal sales and pitch agent using simulated Google ADK patterns.

This repository showcases a fully decoupled, open-source architectural mockup of the proprietary system built during the Google Agentic AI Hackathon. It demonstrates how to design, develop, and deploy an enterprise-grade multimodal pitch deck generator without relying on proprietary Google services.

## The Challenge & Context
This repository showcases a fully decoupled, open-source architectural mockup of the proprietary system built during the Google Agentic AI Hackathon. It demonstrates how to design, develop, and deploy an enterprise-grade multimodal pitch deck generator without relying on proprietary Google services.

## Architecture Diagram (Mermaid Format)
```mermaid
graph TD
    UserInput --> StateInitialization
    StateInitialization --> MarketAnalyzer
    MarketAnalyzer --> Copywriter
    Copywriter --> DeckRenderer
    DeckRenderer --> PitchDeckHTML
    [Style: vertices - 0.1, color - DodgerBlue; edgeStyle - stroke: #333, arrowhead: triangle, arrowsize: 8]
```

## Key Engineering Highlights
- **Google ADK Framework Design:** Decoupling LLMs from custom tool interfaces via a state-based orchestrator.
- **Deterministic Guardrails:** Structured state updates prevent hallucinated pricing or slide content.
- **Cost-Optimized System Design:** Sequential tool execution minimizes compute cycles compared to brute-force agent loops.

## How to Run
1. Clone the repository: `git clone https://github.com/Mo-Ara/agentic-pitch-adk.git`
2. Run the CLI: `python main.py`
3. The tool will prompt for company name and industry, then generate `output/pitch_deck.html` and open it in your default browser.

---
*Created by a Lead AI Engineer – showcasing best practices in agentic system design and MLOps-ready project structure.*