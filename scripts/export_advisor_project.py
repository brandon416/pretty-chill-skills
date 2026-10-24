#!/usr/bin/env python3
"""Build a self-contained ChatGPT Project playbook from three advisor skills.

Run from any directory. Use --check to verify the checked-in export is current.
Standard library only; no network requests or external writes.
"""

import argparse
from pathlib import Path
import re


ROOT = Path(__file__).resolve().parent.parent
DOMAIN = ROOT / "c-level-advisor"
SKILLS = ("cto-advisor", "change-management", "chief-ai-officer-advisor")
OUTPUT = DOMAIN / "project-files" / "PPPT-Executive-Advisors.md"
REPO_URL = "https://github.com/brandon416/pretty-chill-skills/blob/main/"

PROJECT_INSTRUCTIONS = """Use PPPT-Executive-Advisors.md as this project's advisor playbook. Read its
Shared operating rules and the relevant advisor section before answering. Route
architecture, integrations, and technical reliability to CTO Advisor; transitions,
handoffs, and adoption to Change Management; AI prioritization, evaluation, and ROI
to Chief AI Officer Advisor. For mixed questions, combine the relevant lenses
into one recommendation. Use current project evidence before historical defaults.
Proceed with sensible stated assumptions, complete authorized work with available
tools, and be clear about proposals, completed actions, and blockers. Keep the
response practical and give one immediate next action when action is needed.
Do not assume uploaded files grant tool access or create background automations."""


def skill_body(name):
    """Inline the core playbook; turn optional repository resources into URLs."""
    text = (DOMAIN / name / "SKILL.md").read_text(encoding="utf-8")
    text = text.split("---", 2)[2].strip()

    def link(match):
        label, target = match.groups()
        if target == "references/portable-workflow.md":
            return "[Shared operating rules](#shared-operating-rules)"
        if target.startswith(("references/", "scripts/")):
            path = f"c-level-advisor/{name}/{target}"
            return f"[{label} (optional repository reference)]({REPO_URL}{path})"
        return match.group(0)

    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, text)


def render():
    shared = [(DOMAIN / s / "references/portable-workflow.md").read_text(
        encoding="utf-8") for s in SKILLS]
    if len(set(shared)) != 1:
        raise ValueError("Portable rules differ between the standalone skills")
    rules = shared[0].split("\n", 1)[1].strip()
    sections = [
        "# PPPT Executive Advisors",
        "Generated from the three advisor skills by `scripts/export_advisor_project.py`. "
        "Edit the source skills, then regenerate this file.",
        "## Set up your ChatGPT Project\n\n"
        "1. Save this Markdown file and add it to your project's Sources/files.\n"
        "2. Paste the text below into the project's instructions.\n"
        "3. Start a chat inside that project and ask your question in ordinary language.",
        "```text\n" + PROJECT_INSTRUCTIONS + "\n```",
        "## Choose an advisor\n\n"
        "| Question | Advisor |\n| --- | --- |\n"
        "| What should I build, fix, simplify, or connect? | CTO Advisor |\n"
        "| How do I roll this out or hand it off? | Change Management |\n"
        "| What should AI do, and how do we prove its value? | Chief AI Officer Advisor |",
        "## File-only capability\n\n"
        "This file includes all core advisor instructions and shared operating rules. "
        "It supports questions, decisions, drafts, and implementation planning without "
        "the rest of the repository. Optional domain references are linked to GitHub; "
        "they and executable scripts are not embedded. If they are unavailable, "
        "continue with the manual workflow. Code blocks below document repository "
        "commands; uploading this file does not supply those scripts or run them. "
        "A project upload does not install a selectable skill or connect business apps.",
        "## Shared operating rules\n\n" + rules,
    ]
    sections.extend(skill_body(name) for name in SKILLS)
    sections.extend([
        "## Example first question\n\n"
        "> Help me choose the one PPPT workflow to improve this week. Use the relevant "
        "advisors, explain your recommendation, and do the work you can with the "
        "available project files and tools. Tell me exactly what is still missing.",
        "## Platform documentation\n\n"
        "Setup references checked 2026-10-24; recheck current documentation if the UI changes.\n\n"
        "- [OpenAI: Projects and chats](https://learn.chatgpt.com/docs/projects)\n"
        "- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)",
        "## Attribution and license\n\n"
        "Adapted for PPPT from Amin Borghei's advisor skills in the Claude Skills "
        "Library. The original license and Commons Clause condition follow.\n\n"
        "```text\n" + (ROOT / "LICENSE").read_text(encoding="utf-8").strip() + "\n```",
    ])
    return "\n\n".join(sections) + "\n"


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Fail if export is stale")
    args = parser.parse_args()
    content = render()
    if args.check:
        if not OUTPUT.exists() or OUTPUT.read_text(encoding="utf-8") != content:
            parser.exit(1, "Advisor project export is stale; run scripts/export_advisor_project.py\n")
        print("Advisor project export is current")
    else:
        OUTPUT.parent.mkdir(parents=True, exist_ok=True)
        OUTPUT.write_text(content, encoding="utf-8")
        print(f"Wrote {OUTPUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
