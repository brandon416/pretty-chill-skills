# Use the three PPPT advisors

## ChatGPT Project: one file

1. Open [PPPT-Executive-Advisors.md](project-files/PPPT-Executive-Advisors.md).
   Download/save the raw Markdown file from GitHub.
2. Add that file to your ChatGPT project's Sources/files.
3. Copy the project-instructions block near the top of the file into your
   project's instructions. Start a chat inside that project.
4. Ask normally, for example: "What should I automate next?" or "Help me roll
   this process out without more admin work."

The file contains the three core playbooks and their operating rules. Optional
domain references link to GitHub. Scripts are not included. Advice and drafting
work without them; live actions require tools actually available in that chat.
Uploading a file does not install a skill, create a command dropdown, or connect
your apps. Installed skills and project reference files are separate ways to use
the same workflow. No particular model, paid service, or plugin is required by
these playbooks.

## Codex: install the complete folders

Use Codex's skill installer with this prompt:

```text
Install only cto-advisor, change-management, and chief-ai-officer-advisor from
https://github.com/brandon416/pretty-chill-skills under c-level-advisor/.
Keep each complete folder, including references, scripts, agents/openai.yaml,
and LICENSE. Use the skill location supported by this Codex environment.
Inspect existing copies before replacing anything.
```

For current local Codex, repository skills live in `.agents/skills/<name>/` and
user skills in `~/.agents/skills/<name>/`. Hosted environments can provide their
own managed skill installation. These source folders are not automatically
discovered merely because this library is cloned. Avoid duplicate copies with
the same skill name. Use `$cto-advisor`, `$change-management`, or
`$chief-ai-officer-advisor` when installed; `/skills` shows available local skills.
If a change does not appear, restart Codex.

For ChatGPT's installed Skills interface, use the host's skill creator/import
workflow or a supported plugin package. Do not treat project-file upload as
installation, and do not assume GitHub changes automatically update installed
copies. This repository update does not install anything on your Mac.

## Maintain the project copy

After changing a source skill, run from the repository:

```bash
python3 scripts/export_advisor_project.py
python3 scripts/export_advisor_project.py --check
```

Replace the old project file with the newly generated one so the chat does not
have conflicting versions. Each skill carries its own portable rules to remain
standalone; update all three copies together. The exporter rejects differences.
The original Python advisors are retained as optional offline heuristic tools;
their demo and scoring limits are documented in each skill.

Platform references checked 2026-10-24:

- [OpenAI: Build skills](https://learn.chatgpt.com/docs/build-skills)
- [OpenAI: Projects and chats](https://learn.chatgpt.com/docs/projects)
