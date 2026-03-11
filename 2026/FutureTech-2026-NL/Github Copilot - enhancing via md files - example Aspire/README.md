# Github Copilot - enhancing via md files - example: Aspire

## Aspire: AI-enabled

Aspire is roughly for wiring up multi-server and multi-app dotnet (and npm) systems in dev environment
  - they are working on adding deployment support also

However what was more interesting is how they are using Github Copilot for AIAD within the Aspire codebase.

- aspire - src has agent instructions and skills

- aspire.dev

![](./2026-03-11%2013.57.11.jpg)

- https://github.com/dotnet/aspire/tree/main/.github/skills
- https://github.com/dotnet/aspire/blob/main/AGENTS.md

- the Aspire team have invested heavily in Copilot automation, even for fixing flaky tests
- they seem to see CLI as a simpler alternative to MCP (at least, for some cases) since AIs are generally very good at executing CLIs

- can share URL to local server to customer for demos - via dev tunnel (sounds like ssh tunneling).


## Skills vs Custom Agents
![](./2026-03-11%2016.19.13.jpg)

## Copilot helps - you are (still) the architect
![](./2026-03-11%2016.42.11.jpg)


- continuous architecture
  - https://github.com/continuous-architecture/toolkit

- ghc agents and instructions
  - https://github.com/github/awesome-copilot


### AIAD and Architecture

- Maybe try Claude Opus for architecture

- ai skills:
  - c4 diagram designer
  - architecture blueprint generator
  - cloud resource visualiser

- agents

- instructions vs skills:
  - Copilot instructions (e.g., .instructions.md) provide persistent, project-wide rules (coding standards, style) active in all conversations.
  - Conversely, Copilot skills are specialized, task-specific actions (e.g., /run-tests, /debug-pr) invoked on demand via slash commands. Use instructions for constant rules; use skills for workflows
    - skills have an industry standard, agents do not (yet)
