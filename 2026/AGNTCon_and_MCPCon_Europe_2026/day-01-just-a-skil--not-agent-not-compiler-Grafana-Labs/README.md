real topic: just-a-skil--not-agent-not-compiler-Grafana-Labs
official topic: We Built an Agent, We Shipped a Compiler. Here's Why - Joel Verezhak, Grafana Labs

We promised our CX team an agent that would write customer success plans. Six months and four architectures later, we shipped a compiler that calls LLMs in four places.

Each architecture was the right fix for the previous one's failure. The single skill could not enforce quality. The subagents drifted across stages. The scripted prompts hit determinism walls. Only when we accepted that "agentic" was the wrong frame did the output become reviewable, replay-able, and trustworthy enough to ship to real customers.

The talk is a tour of the architectural moments where we learned what LLM-driven systems can and cannot own. Specific failures: a real customer plan shipped with the wrong rows, a quality firewall the LLM kept violating until we made it structural, and "temperature=0" arriving as a footnote rather than a solution.

You leave with three things. A maturity curve from skill to engine. A working distinction between pipeline work and agent work. And a vocabulary for the conversation with stakeholders who keep asking when the agent will be ready, when what they actually want is a compiler with an agentic UI.

Joel Verezhak
Observability Architect, Grafana Labs