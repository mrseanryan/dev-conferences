From Vibes To Data: Evaluating Agents on Your Real Work - Ville Hellman, Datadog

Frontier labs are spending billions making agents better at SWE-Bench. But how much of your engineering work actually looks like SWE-Bench? At Datadog we kept seeing agents that crushed public benchmarks fail on our codebase: missing our conventions, reaching for the wrong internal libraries, technically correct but doing the work the wrong way.

To get past demos and gut feel, we built an evaluation platform that measures agents on tasks drawn from our real work, and gave our platform teams a way to encode best practices as evals. Teams shipping skills, steering docs, agent harnesses, and MCP servers can now see whether their changes actually moved the needle.

In this talk I'll share how SOTA and open-weight models actually compare on real work, what their cost-performance profiles look like, tooling decisions that can shift token usage by 10% or more, and how a surprisingly small eval suite can produce stable signal.

You'll leave with a clearer way to think about model choice as a tradeoff between performance you actually need and tokens you're willing to spend, and a sharper sense of what makes an eval keep paying off over time instead of becoming a one-off exercise.

Ville Hellman
Staff Engineer, Datadog