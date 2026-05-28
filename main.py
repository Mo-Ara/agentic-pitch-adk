#!/usr/bin/env python3
"""
main.py - Runner CLI for Agentic-Pitch-ADK framework.

Provides a professional command-line interface that welcomes the user,
takes inputs, runs the orchestrator pipeline, and launches the HTML deck
in the browser.
"""

import sys
import time
import webbrowser
from pathlib import Path

# Add the project root to the path for imports
sys.path.insert(0, str(Path(__file__).parent))

from app.orchestrator import ADKOrchestrator, Color, log_thought


def print_banner() -> None:
    """Print the application banner."""
    banner = f"""
{Color.CYAN}{Color.BOLD}
╔══════════════════════════════════════════════════════════════════╗
║   🏆 Google Agentic AI Hackathon Runner                       ║
║   Agentic-Pitch-ADK Framework                                 ║
╚══════════════════════════════════════════════════════════════════╝
{Color.RESET}
    This tool generates a beautiful interactive HTML pitch deck
    using simulated ADK patterns and modular agents.
    """
    print(banner)


def get_user_input() -> tuple:
    """
    Prompt the user for target company and industry.
    
    Returns:
        Tuple of (company_name, industry) with defaults applied.
    """
    print(f"{Color.MAGENTA}Please provide the following details:{Color.RESET}")
    
    company = input(f"{Color.YELLOW}Enter the Target Company Name{Color.RESET} [Default: ScoutBot AI]: ").strip()
    industry = input(f"{Color.YELLOW}Enter the Industry/Domain{Color.RESET} [Default: Recruiting & HR Tech]: ").strip()
    
    return company or "ScoutBot AI", industry or "Recruiting & HR Tech"


def print_progress(step: int, total: int, message: str) -> None:
    """Print a progress indicator."""
    bar = "█" * step + "░" * (total - step)
    print(f"{Color.BLUE}[{bar}] {Color.GREEN}{message}{Color.RESET}")


def main() -> None:
    """Main entry point for the CLI runner."""
    print_banner()
    
    # Get user input
    target_company, industry = get_user_input()
    
    print(f"\n{Color.CYAN}🚀 Initializing pipeline for:{Color.RESET}")
    print(f"   Company: {Color.BOLD}{target_company}{Color.RESET}")
    print(f"   Industry: {Color.BOLD}{industry}{Color.RESET}")
    print()

    # Create the orchestrator
    orchestrator = ADKOrchestrator(target_company, industry)

    # Execute pipeline with progress indicators
    total_steps = 3
    
    print_progress(0, total_steps, "Starting Market Analysis...")
    orchestrator.analyze_market()
    time.sleep(0.3)  # Simulate processing time
    
    print_progress(1, total_steps, "Generating Pitch Copy...")
    orchestrator.generate_copy()
    time.sleep(0.3)  # Simulate processing time
    
    print_progress(2, total_steps, "Compiling HTML Deck...")
    orchestrator.compile_deck()
    time.sleep(0.3)  # Simulate processing time

    print_progress(3, total_steps, "Pipeline Complete!")

    # Print execution summary
    print(f"\n{Color.BOLD}{Color.GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Color.RESET}")
    print(f"{Color.BOLD}Pipeline Execution Summary{Color.RESET}")
    print(f"{Color.BOLD}{Color.GREEN}━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━{Color.RESET}")
    print(f"  Total Logs Recorded:   {Color.CYAN}{len(orchestrator.state.logs)}{Color.RESET}")
    print(f"  Artifacts Generated:     {Color.CYAN}{len(orchestrator.state.artifacts_created)}{Color.RESET}")
    print(f"  Generation Time:        ~{Color.CYAN}0.9s{Color.RESET}")
    print(f"  Output Location:        {Color.CYAN}{orchestrator.state.artifacts_created}{Color.RESET}")
    print()

    # Open the HTML deck in the browser
    output_file = orchestrator.state.artifacts_created[0] if orchestrator.state.artifacts_created else None
    if output_file:
        output_path = Path(output_file).resolve()
        print(f"{Color.MAGENTA}🌐 Opening pitch deck in your browser...{Color.RESET}")
        webbrowser.open(f"file://{output_path}")
    else:
        print(f"{Color.RED}⚠️ No output file was generated.{Color.RESET}")

    print(f"\n{Color.GREEN}Thank you for using Agentic-Pitch-ADK!{Color.RESET}")


if __name__ == "__main__":
    main()