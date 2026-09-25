Testing Agents and Their Tools: Offline Evaluation, Synthetic Tasks, and A/B Experiments - Ksenia Bobrova, GitHub

A three-layer evaluation strategy for AI agents and their tools, from experience operating across multiple LLM providers and runtimes.

Offline evaluation: designing benchmark suites with curated requests, expected tool selections, and arguments. Computing precision, recall, F1 scores, confusion matrices for tool mix-ups, and argument hallucination rates to pinpoint description problems.

End-to-end benchmarks: multi-tool flows where the agent chains several calls to complete a task, catching integration regressions that single-tool evaluation misses.

Production A/B experiments: a case study of tool search experiments across OpenAI and Anthropic through staged rollouts. Challenges we hit: caching bugs under real traffic, tool discovery failures, and data skew making early results inconclusive. How we decided whether to advance, pause, or roll back.

These layers compensate for each other's blind spots, forming a testing pyramid that enabled us to safely ship changes to MCP and agent across model providers. Attendees leave with a reusable playbook for testing MCP servers, agents, and running A/B experiments.

Ksenia Bobrova
Senior Software Engineer, GitHub

## Resources

- GitHub: Measuring what matters — offline evaluation of GitHub MCP server: https://github.blog/ai-and-ml/generative-ai/measuring-what-matters-how-offline-evaluation-of-github-mcp-server-works/
- Microsoft Experimentation Platform (EXP): https://www.microsoft.com/en-us/research/group/experimentation-platform-exp/
