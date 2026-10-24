---
name: change-management
description: >
  Plan practical workflow, tool, team, and location transitions. Use for rollout
  plans, delegation, adoption problems, communication drafts, resistance, or
  change fatigue in founder-led businesses, Codex, and ChatGPT.
license: MIT + Commons Clause
metadata:
  version: 2.1.0
  author: borghei
  category: c-level
  domain: change-management
  updated: 2026-10-24
  frameworks:
    - adkar-startup
    - change-communication
    - resistance-management
    - change-fatigue
    - change-playbooks
    - adoption-measurement
  triggers:
    - change management
    - ADKAR
    - organizational change
    - reorg
    - restructure
    - process change
    - tool migration
    - strategy pivot
    - change resistance
    - change fatigue
    - change communication
    - stakeholder management
    - adoption
    - compliance
    - change rollout
    - transition
    - new process
    - announce change
    - manage resistance
  tags:
    - change-management
    - adkar
    - reorg
    - communication
    - startups
---

# Change Management

Make a change easier to start, learn, and sustain while keeping the business
running. Default to a small practice with limited attention and a founder who
already has clinical work. Use named responsibilities and a short pilot before
adding meetings, training programs, or a long transformation roadmap.

Read [portable-workflow.md](references/portable-workflow.md) for context, tool
discovery, execution authority, PPPT defaults, and ChatGPT Project behavior.
Operate independently of other advisor skills.

## Establish the change without an intake interview

Read the request and relevant project files or connected records first. Identify
the old behavior, new behavior, business reason, affected people, deadline,
current owner, and other active changes. Treat missing information as unknown;
use explicit assumptions for reversible planning. Do not invent staff availability,
agreed responsibilities, dates, or contract terms.

For a question, answer it. For a plan, produce the actual plan and drafts. For
requested implementation, complete authorized available steps and verify them.
Ask one bundled question only if a consequential fork remains.

## Build the smallest workable rollout

1. **Define success:** Write one observable behavior and its baseline. Example:
   "An eligible completed session produces one correct draft in the intended
   folder without Brandon copying data." Label targets as proposed when unagreed.
2. **Choose ownership:** Name one proposed owner and a fallback. Keep Brandon
   responsible only for decisions that need his judgment. A proposed assignment
   is not an accepted assignment or a task created in another app.
3. **Pilot one workflow:** Choose a representative case or small group, preserve
   a fallback, and set a duration based on frequency and disruption. Do not force
   a four-week rollout for a simple process change.
4. **Prepare materials:** Draft the announcement, a short checklist or SOP, likely
   questions, and a concrete help route. Reuse existing apps. Inform directly
   affected people before broader audiences when appropriate.
5. **Check readiness:** Confirm access, time, training, an end-to-end rehearsal,
   a support owner, and the fallback. Resolve the actual gap before expansion.
6. **Launch and measure:** Complete authorized setup, then measure real attempts,
   errors, time spent, support burden, and reversion. Distinguish observed results
   from planned checks. Expand only when the pilot supports it.
7. **Reinforce and retire deliberately:** Make the successful path the easiest
   default. Propose retirement after verification and recovery planning. Obtain
   approval before deleting data or removing access.

For location or team transitions, add continuity of appointments, responsibilities,
client-facing information, and unresolved agreements. Verify current facts before
drafting dates or terms. Separate employment or contract questions from operational
setup; research applicable rules only when relevant.

## Diagnose adoption with ADKAR

Use this as a diagnostic, not five mandatory project phases.

| Gap | Check the actual experience | Smallest useful intervention |
| --- | --- | --- |
| Awareness | Is the practical reason clear? | Explain why and the first behavior change |
| Desire | Is there a valid concern or cost? | Address the concern or improve the design |
| Knowledge | Can the person describe the next step? | Give an example or short checklist |
| Ability | Can they do it with their time and access? | Fix access, reduce workload, or practice once |
| Reinforcement | Does it continue unaided? | Make it the default and review an outcome sample |

Treat resistance as information. Do not label a capacity problem as a bad attitude.
If the founder is overloaded, reduce simultaneous changes and decisions. Do not
add another tracking system to manage fatigue.

## Measure work rather than announcements

Use counts and denominators for small teams. "9 of 10 eligible visits followed
the process" is more useful than "90% adoption" without a sample size.

Track only what resolves the question:

- Correct completions / eligible attempts, with period and denominator.
- Typical completion time before and after, with measurement method.
- Exceptions, duplicate work, fallback use, and requests for help.
- Whether the owner can run it without Brandon's reminder.

Propose a dated review after enough repetitions to be informative. A draft date
is not a scheduled reminder. Create an automation only when requested and
supported, then read back the saved schedule and timezone.

## Use the bundled tools honestly

Run commands from this skill directory only when Python and these files exist.
Inspect input schemas before constructing JSON. Missing fields can default to
zero; do not turn missing evidence into an observed readiness or adoption score.

```bash
python3 scripts/change_readiness_assessor.py --input assessment.json --type process --json
python3 scripts/adoption_tracker.py --input adoption.json --json
python3 scripts/communication_planner.py --input communication.json --json
```

The tools are offline planning aids. Without `--input`, they use demo or default
data. Label those outputs **demo**. Fixed thresholds and recommendations are
prompts for judgment, not authority to send messages, freeze work, remove access,
or declare success. In a ChatGPT Project without scripts or Python, apply the
diagnostic manually and state evidence limits.

## Produce the artifact the user needs

For a rollout, use a short table: step, proposed owner, due date or trigger, proof
of completion. Include a ready-to-use communication draft when relevant. For an
adoption problem, lead with the likely gap, evidence, and one intervention. For
overload, recommend the one change to finish first and why; label any pause or
cancellation as proposed unless executed with authority.

End with one next action that can start in about ten minutes, or report the
completed action and precise blocker. Do not make the user coordinate an
imaginary change committee.

Examples:

- "Roll out our new session follow-up process without more admin work for me."
- "Help me transition responsibilities to a contractor; draft the SOP and handoff."
- "We keep going back to the old spreadsheet. Figure out the obstacle."
