#!/usr/bin/env python3
"""
copywriter.py - Simulated copywriting tool for Agentic-Pitch-ADK.

This tool generates structured sales pitch content based on market research data,
then updates the orchestrator state with the generated pitch structure.
"""

from typing import Dict, Any, List


class Copywriter:
    """
    Simulates AI-powered copywriting by generating structured pitch content
    based on market research data.
    
    The tool synthesizes market insights into compelling sales narrative
    with slide-by-slide content and visual prompts.
    """

    def __init__(self, target_company: str, industry: str):
        """
        Initialize the copywriter with context parameters.
        
        Args:
            target_company: Name of the target company/product
            industry: Industry/domain classification
        """
        self.target_company = target_company
        self.industry = industry

    def run(self, state) -> Dict[str, Any]:
        """
        Execute copywriting and update the state.
        
        Args:
            state: The orchestrator state containing market_research
            
        Returns:
            Updated state dictionary with pitch_copy populated
        """
        # Check if market research is available
        if not state.market_research:
            log_thought("Copywriter", "Error", 
                       "Market research not available - skipping copywriting")
            return {}
        
        log_thought("Copywriter", "Initiation", 
                   f"Starting copywriting for {self.target_company} in {self.industry}")

        # Generate pitch content based on market research
        pitch_content = self._generate_pitch_content(state.market_research)

        # Update state with generated content
        state.pitch_copy = pitch_content
        state.logs.append("Copywriting completed successfully")
        
        log_thought("Copywriter", "Completion", 
                   f"Generated structured pitch with {len(pitch_content['slides'])} slides")
        
        return state.pitch_copy

    def _generate_pitch_content(self, market_research: Dict[str, Any]) -> Dict[str, Any]:
        """
        Generate structured pitch content based on market research.
        
        Args:
            market_research: Dictionary containing market analysis data
            
        Returns:
            Dictionary with structured pitch content
        """
        # Create compelling tagline based on industry
        tagline = self._create_tagline()
        
        # Generate problem statement
        problem_statement = self._create_problem_statement(market_research)
        
        # Generate solution statement
        solution_statement = self._create_solution_statement(market_research)
        
        # Generate slide content
        slides = self._create_slides(market_research)
        
        return {
            "tagline": tagline,
            "problem_statement": problem_statement,
            "solution_statement": solution_statement,
            "slides": slides
        }

    def _create_tagline(self) -> str:
        """Create an impactful tagline for the company."""
        industry_specific_taglines = {
            "fintech": "Transform Finance with Intelligent Automation",
            "healthtech": "Healthcare Innovation Powered by AI",
            "ai": "Intelligence Engineered for Tomorrow",
            "edtech": "Education Personalized, Performance Optimized"
        }
        
        tagline = industry_specific_taglines.get(
            self.industry.lower(), 
            f"Transform {self.industry} with Intelligent Automation"
        )
        
        return f"{tagline} - {self.target_company}"

    def _create_problem_statement(self, market_research: Dict[str, Any]) -> str:
        """Create a compelling problem statement based on pain points."""
        pain_points = market_research.get("pain_points", [])
        
        problem_intro = f"Companies in {self.industry} face significant challenges that prevent growth and innovation. "
        
        pain_point_descriptions = []
        for i, pain_point in enumerate(pain_points, 1):
            pain_point_descriptions.append(f"• {pain_point}")
        
        pain_part = " ".join(pain_point_descriptions)
        
        problem_outro = f"These challenges result in reduced efficiency, higher costs, and missed opportunities in the {market_research.get('market_size', 'marketplace')}."
        
        return f"{problem_intro}{pain_part} {problem_outro}"

    def _create_solution_statement(self, market_research: Dict[str, Any]) -> str:
        """Create a solution statement that addresses the pain points."""
        opportunities = market_research.get("opportunities", [])
        
        solution_intro = f"{self.target_company} provides a comprehensive solution that directly addresses these challenges by offering "
        
        opportunity_descriptions = []
        for i, opportunity in enumerate(opportunities, 1):
            opportunity_descriptions.append(f"• {opportunity}")
        
        opportunity_part = " ".join(opportunity_descriptions)
        
        solution_outro = f"This approach enables organizations to transform their operations, reduce costs, and capture new market opportunities in {self.industry}."
        
        return f"{solution_intro}{opportunity_part} {solution_outro}"

    def _create_slides(self, market_research: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Create structured slide content with visual prompts."""
        market_size = market_research.get("market_size", "Market size unspecified")
        competitors = market_research.get("competitors", [])
        pain_points = market_research.get("pain_points", [])
        opportunities = market_research.get("opportunities", [])
        
        slides = [
            {
                "slide_id": 1,
                "title": "Market Opportunity",
                "content": [
                    f"Addressable Market: {market_size}",
                    "Key Competitors Identified:",
                    *[f"  • {competitor}" for competitor in competitors],
                    "Market Entry Points:",
                    *[f"  • {opportunity}" for opportunity in opportunities]
                ],
                "visual_prompt": "Modern dashboard showing market size metrics, competitor landscape visualization, and opportunity matrix"
            },
            {
                "slide_id": 2,
                "title": "The Challenge",
                "content": [
                    "Current Industry Pain Points:",
                    *[f"  • {pain_point}" for pain_point in pain_points],
                    "Impact on Businesses:",
                    "  • Reduced operational efficiency",
                    "  • Higher acquisition costs",
                    "  • Limited innovation potential"
                ],
                "visual_prompt": "Dark-themed infographic showing pain point hierarchy and business impact metrics"
            },
            {
                "slide_id": 3,
                "title": "Our Solution",
                "content": [
                    f"{self._create_tagline()}",
                    "Core Solution Components:",
                    "  • AI-powered automation engine",
                    "  • Seamless integration capabilities",
                    "  • Industry-specific optimization",
                    "  • Scalable architecture"
                ],
                "visual_prompt": "Clean interface mockup showing modern dashboard with AI-powered features and integration points"
            },
            {
                "slide_id": 4,
                "title": "Go-to-Market Strategy",
                "content": [
                    "Phased Approach:",
                    "  • Phase 1: Target key industry verticals",
                    "  • Phase 2: Partnership ecosystem development",
                    "  • Phase 3: Global expansion",
                    "Success Metrics:",
                    "  • User acquisition targets",
                    "  • Revenue growth projections",
                    "  • Market share goals"
                ],
                "visual_prompt": "Strategic roadmap timeline with phase milestones and key performance indicators"
            },
            {
                "slide_id": 5,
                "title": "Why Choose Us",
                "content": [
                    "Competitive Advantages:",
                    "  • Proprietary AI technology",
                    "  • Deep industry expertise",
                    "  • Proven track record",
                    "  • Enterprise-grade security",
                    "  • Ongoing innovation pipeline",
                    f"Partnerships with leading {self.industry} providers"
                ],
                "visual_prompt": "Competitive matrix visualization showing advantages over traditional solutions"
            }
        ]
        
        return slides


# Simple log_thought function for standalone testing
def log_thought(agent_name: str, step: str, message: str) -> None:
    """
    Print a formatted log entry for standalone testing.
    """
    print(f"[{agent_name}] → {step}: {message}")