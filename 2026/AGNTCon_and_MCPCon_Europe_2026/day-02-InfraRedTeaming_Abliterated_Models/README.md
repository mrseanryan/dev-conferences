Infrastructure Red Teaming With Abliterated Models: What Actually Stops Agent Attacks - Roy Belio, Red Hat

Safety-aligned models refuse adversarial prompts, so you can't test whether your infrastructure controls actually work, but the models are all still susceptible to jail-breaking.
I removed that variable with an abliterated Qwen3.5 model to get zero refusals and 100% cooperation. Ran full suite of prompts with custom garak probes across three hardening tiers on an OpenClaw agent running in OpenShift.

I found out what worked and what gave false sense of security.
Sandbox isolation dropped credential exfiltration entirely in one step. NetworkPolicy killed cluster escalation. The prompt injection classifier caught encoding-based attacks. Three of four attack categories were fully stopped by Tier 2 (injection classification+isolation).

Memory poisoning was the exception. Probes that instruct the agent to write attacker content into its own memory continued to succeed across all tiers. OWASP added this as ASI06 to its 2026 Agentic Top 10. No deployed control addresses it today.

I'll present the full probe results, the defense configurations, and the open problem current agent architectures don't solve.

Roy Belio
Senior Software Engineer, Red Hat

## Resources

- Session details (Sched): https://agntconmcpconeu26.sched.com/event/2RBBJ/infrastructure-red-teaming-with-abliterated-models-what-actually-stops-agent-attacks-roy-belio-red-hat
- OpenClaw + Abliterated LLM Red Team (OpenShift): https://github.com/aicatalyst-team/openclaw-openshift-redteam

## Notes

- Classifiers and guardrails are not sufficient; non-English/encoded inputs bypass them.
- Isolation (sandboxing) and network policies were highly effective at stopping several categories.
- Memory poisoning remained unsolved across tiers; OWASP ASI06 highlights this class.
- Canary data can help detect compromise when it leaks into logs or outputs.
