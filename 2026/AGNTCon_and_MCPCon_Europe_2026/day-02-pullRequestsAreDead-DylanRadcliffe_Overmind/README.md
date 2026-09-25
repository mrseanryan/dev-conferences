Pull Requests Are Dead, Long Live Peer Review - Dylan Ratcliffe, Overmind

When AI writes 80–90% of the code on a team, peer review breaks. The pull request is produced by a machine you can't argue with, and the reviewer is auditing a diff instead of talking to a peer. Review has stopped feeling like collaboration, and most of us have started hating it.

We rebuilt how we deploy AI-assisted development in production. Human review moved off the diff and onto the plan: the intent written before any code gets generated. Engineers review the thinking they care about and let the agent fill in the gaps. When the PR lands, CI runs the usual checks plus an automated comparison against the approved plan. Only deviations route back to the original reviewer.

This is a case study in integrating AI into a real SDLC without breaking accountability, quality, or culture. I'll walk through what broke, what we automated, and what stayed human: an in-house MCP server for plan review in the IDE, deviation-checking on every PR, and cultural bets (everyone operates as a team lead; no questions until working code; customer context radiated to the whole team).

We massively improved our velocity and our lead time, and our engineers love the job again.

Dylan Ratcliffe
Founder & CEO, Overmind