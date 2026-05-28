#!/usr/bin/env python3
"""
orchestrator.py - Core state machine for the Agentic-Pitch-ADK framework.

This file implements the Google Agent Development Kit (ADK) pattern:
- State tracking for the current project context
- Sequential execution of specialized tool nodes
- Rich, colorized logging of agent thought processes
"""

import os
import sys
from dataclasses import dataclass, field
from typing import List, Dict, Any
from pathlib import Path

# ANSI color codes for terminal output
class Color:
    """ANSI color codes for terminal output."""
    RESET = "\033[0m"
    GREEN = "\033[32m"
    CYAN = "\033[36m"
    MAGENTA = "\033[35m"
    YELLOW = "\033[33m"
    RED = "\033[31m"
    BLUE = "\033[34m"
    BOLD = "\033[1m"

def colorize(text: str, color_code: str) -> str:
    """Wrap text with ANSI color codes."""
    return f"{color_code}{text}{Color.RESET}"

def log_thought(agent_name: str, step: str, message: str) -> None:
    """
    Print a formatted log entry simulating agentic execution.
    
    Args:
        agent_name: Name of the agent performing the action
        step: Description of the current step
        message: Detailed message about the action
    """
    colored_agent = colorize(f"[{agent_name}]", Color.CYAN)
    colored_step = colorize(f"→ {step}", Color.YELLOW)
    colored_msg = colorize(message, Color.GREEN)
    
    print(f"{Color.BOLD}{colored_agent} {colored_step} {colored_msg}{Color.RESET}")

@dataclass
class AgentState:
    """
    Represents the current state of the agentic workspace.
    
    Attributes:
        target_company: Name of the target company/product
        industry: Industry/domain classification
        market_research: Dictionary containing market analysis data
        pitch_copy: Dictionary containing generated pitch content
        artifacts_created: List of file paths created during execution
        logs: List of log messages documenting agent execution
    """
    target_company: str = ""
    industry: str = ""
    market_research: Dict[str, Any] = field(default_factory=dict)
    pitch_copy: Dict[str, Any] = field(default_factory=dict)
    artifacts_created: List[str] = field(default_factory=list)
    logs: List[str] = field(default_factory=list)

class ADKOrchestrator:
    """
    Main orchestrator class that manages the state machine and sequential execution
    of agentic tools.
    """
    
    def __init__(self, target_company: str, industry: str):
        """
        Initialize the orchestrator with target context.
        
        Args:
            target_company: Name of the target company/product
            industry: Industry/domain classification
        """
        self.state = AgentState(
            target_company=target_company,
            industry=industry,
            market_research={},
            pitch_copy={},
            artifacts_created=[],
            logs=[]
        )
        log_thought("System", "Initialization", 
                   f"Starting Agentic-Pitch-ADK workflow for {target_company} in {industry}")

    def log_thought(self, agent_name: str, step: str, message: str) -> None:
        """
        Log a thought from an agent with formatted terminal output.
        
        Args:
            agent_name: Name of the agent
            step: Description of the current step
            message: Detailed message about the action
        """
        self.state.logs.append(message)
        log_thought(agent_name, step, message)

    def analyze_market(self) -> None:
        """
        Simulate market analysis by running the MarketAnalyzer tool.
        This step populates the market_research field in state.
        """
        log_thought("Market Analyzer", "Analyzing market trends", 
                   "Running market analysis for target company...")
        
        # Simulate tool execution - in real implementation this would call market_analyzer.run()
        market_data = {
            "market_size": "$120B Addressable Market",
            "competitors": [
                "Competitor A - Established leader",
                "Competitor B - Emerging startup",
                "Competitor C - Niche specialist"
            ],
            "pain_points": [
                "Fragmented user experience",
                "High customer acquisition costs",
                "Limited personalization capabilities"
            ],
            "opportunities": [
                "AI-driven personalization",
                "API-first integration model",
                "Vertical-specific solution bundles"
            ]
        }
        
        # Update state and log completion
        self.state.market_research = market_data
        self.state.logs.append("Market analysis completed successfully")
        log_thought("Market Analyzer", "Completion", 
                   "Retrieved 3 competitor profiles and analyzed TAM")

    def generate_copy(self) -> None:
        """
        Simulate copywriting by generating structured pitch content.
        This step uses the market research to create pitch structure.
        """
        log_thought("Copywriter", "Generating pitch content", 
                   "Synthesizing market insights into sales narrative...")
        
        # Build pitch structure from market data
        pitch_content = {
            "tagline": f"Transform {self.state.industry.lower()} with intelligent automation",
            "problem_statement": (
                f"Companies in {self.state.industry} struggle with "
                f"fragmented workflows, high acquisition costs, and limited personalization. "
                f"The pain points of {', '.join(self.state.market_research['pain_points'])} "
                f"create significant revenue leakage."
            ),
            "solution_statement": (
                f"Our platform solves these challenges by providing "
                f"AI-powered personalization, API-first integration, and vertical-specific solutions. "
                f"By addressing {', '.join(self.state.market_research['pain_points'])}, "
                f"we enable {self.state.target_company} to capture new market opportunities."
            ),
            "slides": [
                {
                    "slide_id": 1,
                    "title": "The Opportunity",
                    "content": [
                        "Massive TAM of $120B in the {self.state.industry} market",
                        "3 key pain points affecting 85% of enterprises",
                        "3 high-leverage entry points for market capture"
                    ],
                    "visual_prompt": "Modern dashboard showing market size metrics and trend analysis"
                },
                {
                    "slide_id": 2,
                    "title": "Our Solution",
                    "content": [
                        "AI-driven personalization engine",
                        "API-first architecture for seamless integration",
                        "Vertical-specific solution bundles"
                    ],
                    "visual_prompt": "Clean interface mockup showing personalized user experience"
                },
                {
                    "slide_id": 3,
                    "title": "Go-to-Market Strategy",
                    "content": [
                        "Targeted industry verticals first",
                        "Partnerships with key ecosystem players",
                        "Freemium model to drive adoption"
                    ],
                    "visual_prompt": "Marketing funnel diagram with conversion metrics"
                }
            ]
        }
        
        self.state.pitch_copy = pitch_content
        self.state.logs.append("Copywriting completed successfully")
        log_thought("Copywriter", "Completion", 
                   "Generated structured pitch with 3 slides and visual prompts")

    def compile_deck(self) -> None:
        """
        Simulate deck compilation by creating a placeholder HTML file.
        In a real implementation this would generate a full interactive presentation.
        """
        log_thought("Deck Renderer", "Compiling presentation", 
                   "Creating interactive HTML slide deck...")
        
        # Create output directory if it doesn't exist
        output_dir = Path("output")
        output_dir.mkdir(parents=True, exist_ok=True)
        
        # Create simple HTML template with injected content
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{self.state.target_company} Pitch Deck</title>
    <link href="https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css" rel="stylesheet">
    <style>
        body {{ background-color: #1f2937; color: #f3f4f6; }}
        .slide {{ background-color: #111827; border: 1px solid #374151; margin: 2rem; padding: 1.5rem; border-radius: 8px; }}
        .title {{ color: #10b981; font-size: 1.5rem; margin-bottom: 1rem; }}
        .content {{ color: #e5e7eb; line-height: 1.6; }}
        .visual {{ border: 1px solid #374151; border-radius: 4px; padding: 1rem; margin: 1rem 0; }}
    </style>
</head>
<body>
    <div class="container mx-auto px-4 py-8">
        <h1 class="text-4xl text-center font-bold text-green-400 mb-8">{self.state.target_company}</h1>
        
        <!-- Slide 1: The Opportunity -->
        <div class="slide">
            <div class="title">The Opportunity</div>
            <div class="content">
                <ul>
                    <li>Massive TAM of {self.state.market_research['market_size']} in the {self.state.industry} market</li>
                    <li>3 key pain points affecting 85% of enterprises</li>
                    <li>3 high-leverage entry points for market capture</li>
                </ul>
            </div>
            <div class="visual">
                <!-- Visual placeholder -->
                Market Analysis Dashboard
            </div>
        </div>

        <!-- Slide 2: Our Solution -->
        <div class="slide">
            <div class="title">Our Solution</div>
            <div class="content">
                <ul>
                    <li>AI-driven personalization engine</li>
                    <li>API-first architecture for seamless integration</li>
                    <li>Vertical-specific solution bundles</li>
                </ul>
            </div>
            <div class="visual">
                <!-- Visual placeholder -->
                Modern interface mockup
            </div>
        </div>

        <!-- Slide 3: Go-to-Market Strategy -->
        <div class="slide">
            <div class="title">Go-to-Market Strategy</div>
            <div class="content">
                <ul>
                    <li>Targeted industry verticals first</li>
                    <li>Partnerships with key ecosystem players</li>
                    <li>Freemium model to drive adoption</li>
                </ul>
            </div>
            <div class="visual">
                <!-- Visual placeholder -->
                Marketing funnel diagram
            </div>
        </div>

        <!-- Interactive Agent Logs Dashboard -->
        <div class="slide">
            <div class="title">Agentic Logs Dashboard</div>
            <div class="content">
                <pre>{self._format_logs()}</pre>
            </div>
        </div>
    </div>
</body>
</html>"""

        # Write HTML file
        output_file = output_dir / "pitch_deck.html"
        output_file.write_text(html_content, encoding="utf-8")
        
        self.state.artifacts_created.append(str(output_file))
        self.state.logs.append("Deck compilation completed successfully")
        log_thought("Deck Renderer", "Completion", 
                   f"Successfully compiled interactive pitch deck artifact to {output_file}")

    def _format_logs(self) -> str:
        """
        Format the logs for display in the HTML dashboard.
        """
        if not self.state.logs:
            return "No logs recorded"
        formatted = "\n".join(f"• {log}" for log in self.state.logs)
        return formatted

    def run_pipeline(self) -> None:
        """
        Execute the complete agentic workflow in sequence.
        """
        log_thought("Orchestrator", "Pipeline Start", 
                   "Beginning end-to-end workflow execution...")

        self.analyze_market()
        self.generate_copy()
        self.compile_deck()

        log_thought("Orchestrator", "Pipeline Complete", 
                   f"Workflow completed for {self.state.target_company} in {self.state.industry}")
        print(f"\n{Color.GREEN}✅ Pipeline execution complete!{Color.RESET}")
        print(f"Artifacts created: {len(self.state.artifacts_created)}")
        print(f"Logs recorded: {len(self.state.logs)}")

def main() -> None:
    """
    Main entry point for the orchestrator.
    """
    # Default values - can be overridden via CLI in main.py
    default_company = "ScoutBot AI"
    default_industry = "Recruiting & HR Tech"

    print(colorize("🚀 Agentic-Pitch-ADK Framework", Color.MAGENTA + Color.BOLD))
    print(f"Target Company: {colorize(default_company, Color.CYAN)}")
    print(f"Industry: {colorize(default_industry, Color.CYAN)}")
    print()

    orchestrator = ADKOrchestrator(default_company, default_industry)
    orchestrator.run_pipeline()

if __name__ == "__main__":
    main()