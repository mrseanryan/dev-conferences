Agents Talking To Agents: MCP, A2A, and the Reality of Multi-Agent Orchestration in Production - Willem Berroubache, Orange

Building a multi-agent system in a notebook is straightforward
Running one on production infrastructure, where a wrong handoff triggers a real incident, is a different problem entirely.

This talk shares hard-won lessons from deploying autonomous agents using both MCP and A2A protocols in a large-scale, regulated environment.
We move past the happy path and focus on what actually breaks: agents that lose task context mid-chain, trust boundaries that collapse during agent-to-agent delegation, tool conflicts between concurrent agents, and orchestration failures that only surface under real load.
We walk through three patterns that emerged from this work. How to split responsibilities between MCP and A2A so each protocol does what it is actually good at. How to scope agent authority using MCP server boundaries without creating coordination bottlenecks. And how to design agent-to-agent handoffs that degrade gracefully when part of the chain fails mid-task.

No toy examples. No vendor pitches. Concrete decisions, the tradeoffs behind them, and what we would change today. Attendees leave with patterns they can apply the next day, regardless of their agent framework.

Willem Berroubache
AI for Security Project Manager, Orange

## Resources

- MCP organization repositories: https://github.com/orgs/modelcontextprotocol/repositories
- MCP extension: Tasks (hibernate/auto-wake agents): https://github.com/modelcontextprotocol/ext-tasks
- MCP experimental extension: Triggers & Events: https://github.com/modelcontextprotocol/experimental-ext-triggers-events
