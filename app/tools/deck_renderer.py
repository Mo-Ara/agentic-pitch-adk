#!/usr/bin/env python3
"""
deck_renderer.py - Simulated deck rendering tool for Agentic-Pitch-ADK.

Creates an interactive HTML presentation using Tailwind CSS and injects the
generated pitch content into a polished slide deck.
"""

from pathlib import Path
from typing import Dict, Any


def log_thought(agent_name: str, step: str, message: str) -> None:
    """Print a formatted log entry for standalone execution or debugging."""
    print(f"[{agent_name}] → {step}: {message}")


class DeckRenderer:
    """Render a beautiful, responsive HTML pitch deck from orchestrator state."""

    def __init__(self, output_dir: Path = Path("output")):
        self.output_dir = output_dir
        self.output_dir.mkdir(parents=True, exist_ok=True)

    def run(self, state) -> str:
        """
        Generate the HTML deck and return the path to the created file.
        
        Args:
            state: Orchestrator state containing target_company, industry,
                   market_research, and pitch_copy.
        
        Returns:
            Path to the generated HTML file as a string.
        """
        log_thought("Deck Renderer", "Initiation", 
                   f"Rendering HTML deck for {state.target_company} ({state.industry})")
        
        html_content = self._build_html(state)
        output_path = self.output_dir / "pitch_deck.html"
        output_path.write_text(html_content, encoding="utf-8")
        
        # Update state tracking
        state.artifacts_created.append(str(output_path))
        state.logs.append("Deck rendering completed successfully")
        
        log_thought("Deck Renderer", "Completion", 
                   f"Successfully compiled interactive pitch deck artifact to {output_path}")
        
        return str(output_path)

    # --------------------------------------------------------------------- #
    # Internal helpers
    # --------------------------------------------------------------------- #
    def _build_html(self, state) -> str:
        """Construct the HTML content."""
        # Helper to safely escape braces for any future f-string processing
        def esc(text: str) -> str:
            return text.replace("{", "{{").replace("}", "}}")

        pc = state.pitch_copy or {}
        mr = state.market_research or {}

        # Transform slides data into robust HTML markup
        slides_html_parts = []
        for slide in pc.get("slides", []):
            title = esc(slide.get("title", ""))
            bullet_items = slide.get("content", [])
            bullet_html = "".join(f"<li>{esc(item)}</li>" for item in bullet_items)
            visual_prompt = esc(slide.get("visual_prompt", ""))
            slide_html = (
                "<div class=\"slide\">\n"
                f"    <div class=\"title\">{title}</div>\n"
                f"    <div class=\"content\"><ul>{bullet_html}</ul></div>\n"
                f"    <div class=\"visual\"><em>{visual_prompt}</em></div>\n"
                f"</div>\n"
            )
            slides_html_parts.append(slide_html)

        slides_html = "".join(slides_html_parts)
        if not slides_html:
            slides_html = "<p>No slide content generated.</p>"

        # Build formatted logs for display
        logs_text = "\\n".join(state.logs)
        logs_formatted = esc(logs_text)

        # Build final HTML with Tailwind CDN and simple styling
        html = (
            "<!DOCTYPE html>\n"
            "<html lang=\"en\">\n"
            "<head>\n"
            "    <meta charset=\"UTF-8\">\n"
            "    <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n"
            f"    <title>{esc(state.target_company)} Pitch Deck</title>\n"
            "    <link href=\"https://cdn.jsdelivr.net/npm/tailwindcss@2.2.19/dist/tailwind.min.css\" rel=\"stylesheet\">\n"
            "    <style>\n"
            "        body { background-color: #1f2937; color: #f3f4f6; }\n"
            "        .slide { background-color: #111827; border: 1px solid #374151; \n"
            "                 margin: 2rem; padding: 1.5rem; border-radius: 8px; }\n"
            "        .title { color: #10b981; font-size: 1.5rem; margin-bottom: 1rem; }\n"
            "        .content { color: #e5e7eb; line-height: 1.6; }\n"
            "        .visual { border: 1px solid #374151; border-radius: 4px; \n"
            "                  padding: 1rem; margin: 1rem 0; }\n"
            "    </style>\n"
            "</head>\n"
            "<body>\n"
            "    <div class=\"container mx-auto px-4 py-8\">\n"
            f"        <h1 class=\"text-4xl text-center font-bold text-green-400 mb-8\">{esc(state.target_company)}</h1>\n"
            f"{slides_html}\n"
            "        <div class=\"slide\">\n"
            "            <div class=\"title\">Agentic Logs Dashboard</div>\n"
            "            <div class=\"content\">\n"
            f"                <pre>{logs_formatted}</pre>\n"
            "            </div>\n"
            "        </div>\n"
            "    </div>\n"
            "</body>\n"
            "</html>"
        )
        return html