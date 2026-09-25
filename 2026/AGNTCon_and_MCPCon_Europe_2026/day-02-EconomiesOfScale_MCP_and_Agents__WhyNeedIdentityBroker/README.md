Economies of Scale for MCP and Agents: Why You Need an Identity Broker - Magnus Jungsbluth & Jan Brennenstuhl, Zalando SE

Drawing from lessons of how to scale an enterprise to thousands of microservices, we make the case that pushing concerns to the infrastructure for agentic systems should be a no-brainer when planning to scale agentic systems.
This talk explores how Zalando tackled this challenge by building and open-sourcing our own agentic identity broker as part of our broader agentic platform initiative. We will share how it supports delegation chains across third-party and in-house applications, integrates with the CNCF project agentgateway and how it allows us to keep these pesky authentication / authorization concerns on the infrastructure and keep MCP servers and agents simple.
We will dive into the technical mechanics, how it integrates into a larger enterprise and allows us to apply just enough governance to stay ahead of the game. We will cover practical applications and limitations of dynamic client registration.
A closing outlook will illustrate how tool approvals and human-in-the-loop can be enforced centrally without agent authors or MCP authors having to build anything. Practical examples of CIBA and intent-based access will complete the session.

Magnus Jungsbluth
Senior Principal Engineer, Zalando SE

Jan Brennenstuhl
Principal Software Engineer, Zalando SE

## Resources

- Agentic Identity Broker (Zalando) repository: https://github.com/zalando-incubator/agentic-identity-broker
- Agentic Identity Broker site: https://agenticidentitybroker.dev/
