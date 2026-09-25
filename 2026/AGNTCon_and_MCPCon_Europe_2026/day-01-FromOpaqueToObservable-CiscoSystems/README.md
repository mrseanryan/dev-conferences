From Opaque To Observable: Tracing Multi-Agent OpenClaw Workflows With OpenTelemetry - Jordan Augé, Cisco Systems

Agent systems are getting more capable, but they are still hard to operate when a single user request fans out across multiple agents, tools, model calls, queues, and outbound messages. In this session, we will walk through how we built an open observability plugin for OpenClaw (InsightClaw) that turns that opaque execution path into a connected telemetry story using OpenTelemetry.

The talk covers a practical design that combines three signal paths: typed lifecycle hooks for request, agent, tool, and response flow; diagnostics events for model usage, cost, queue, webhook, and stuck-session signals; and optional provider SDK auto-instrumentation for GenAI calls. Together, these produce connected traces, useful operational metrics, and cross-session lineage for handoffs, spawned subagents, and parallel branches.

We will show the trace model we used, the session semantics we had to define for real workflows, and the engineering tradeoffs around payload capture, runtime patching, and correlating control-plane events with agent execution.


Jordan Augé
Tech Lead, Outshift@Cisco - Chair of Accuracy and Reliabiity WG, Cisco Systems
