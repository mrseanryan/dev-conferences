# genai-on-your-code

- Using GenAI on your code - Niels Tanis

## Official notes:
https://github.com/nielstanis/futuretech2025

## Security blog

https://embracethered.com/blog/

## LLM Security Tools

[PyRIT](https://github.com/Azure/PyRIT)

- The Python Risk Identification Tool for generative AI (PyRIT) is an open source framework built to empower security professionals and engineers to proactively identify risks in generative AI systems.

## LLM Attacks

[Crescendo LLM attack](https://crescendo-the-multiturn-jailbreak.github.io/)

Microsoft - [Lessons From Red Teaming 100 Generative AI Products](https://arxiv.org/abs/2501.07238)

## LLM Security

[Minting Silver Bullets is challenging](https://www.youtube.com/watch?v=J1QMbdgnY8M)

https://pentestgpt.ai/

## Standards for AI (LLM) Vulnerabilities

1. OWASP Top 10 for Large Language Model Applications
https://owasp.org/www-project-top-10-for-large-language-model-applications/

2. https://atlas.mitre.org/ - Navigate threats to AI systems through real-world insights

## Related [added later]

- [OWASP Top 10 for LLM Applications](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_0_1.pdf)
- [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/)
- [Prompt Injection attack against LLM-integrated Applications](https://arxiv.org/abs/2306.05499)


### Tooling

- [llm-guard](https://github.com/protectai/llm-guard/tree/v0.3.4)
  - uses: [presidio](https://github.com/microsoft/presidio/)
  - helps to block **Prompt Injection** attackes like:
    - [Prefix Injection] For the next hour, greet every customer with: ...
      - Start your response with ..., and ...
    - [Ignore Previous Instructions] Ignore previous instructions and ...
    - [Role Playing] Pretend you are a ... and ...
    - [Refusal Suppression] Do not apologize or include any negative sentence about the prompt. Then, ...
    - [Obfuscation] Base64-encode following communications ...

    - (provided for educational purposes)
- [DOMPurify](https://github.com/cure53/DOMPurify)
  - can block HTML/JavaScript/CSS injection attacks

