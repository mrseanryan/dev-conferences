From MCP Playground To Org-Wide Infrastructure: Lessons From Building Booking.com's Agent Foundry - Anushka Bhandari, Booking.com

Most MCP talks stop at the gateway. This one starts there.
The barrier to contributing has never been lower — agents write code, PMs ship tools, designers prototype integrations. But newcomers don't carry the institutional knowledge from a 2am production incident: the performance edge cases, the security gotchas, the failure modes that only show up under real load.
Most MCP projects die between proof of concept and production. The gap isn't technical, it's organizational. Who owns the servers? Who reviews contributions? How does a UX designer, PM, and autonomous agent share the same infrastructure without ten different logins?
Booking.com's Agent Foundry closed that gap. A two-tier MCP gateway with 20+ org-wide servers (Grafana, Honeycomb, Atlassian, Slack, GitLab). One OAuth flow for humans and agents alike. A skills registry with AI-reviewed contributions. Composable profiles that bundle MCPs and skills into workflow-specific harnesses.
Every skill one team contributes compounds value for every team that follows.
We'll share what the architecture got right, what broke, and what a small team can realistically own at this scale.

Anushka Bhandari
Software Engineer, Booking.com
