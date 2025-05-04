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

- [OWASP for LLM Applications - 2025](https://genai.owasp.org/llm-top-10/)
- [OWASP for LLM Applications - 2023](https://owasp.org/www-project-top-10-for-large-language-model-applications/)
- [OWASP for LLM Applications - 2023](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-2023-v1_0_1.pdf)

3. https://atlas.mitre.org/ - Navigate threats to AI systems through real-world insights

## Related [added later]
- [Threat Modeling LLM Applications](https://aivillage.org/large%20language%20models/threat-modeling-llm/)
- [Multi-Agentic system Threat Modeling Guide v1.0](https://genai.owasp.org/resource/multi-agentic-system-threat-modeling-guide-v1-0/)
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
    - [Universal Adversarial Attacks] (adding special character sequences to the prompt - can discover them via brute force permutations)
    - (provided for educational purposes)
- [DOMPurify](https://github.com/cure53/DOMPurify)
  - can block HTML/JavaScript/CSS injection attacks

### Defensive Measures
Based on the excellent security courses at https://www.secureflag.com/.

- Classification Models: use text classification models to detect attacks against LLMs by scanning the input prompts and outputs of the LLM.
- Prompts defense: Write comprehensive and robust original prompts for the LLM. Tell the LLM to be cautious by anticipating potential attacks. Also, try reiterating the original instructions using post-prompting.
- Wrapping user input: enclose the user input between separators, such as random strings or XML tags - this is to help the LLM differentiate user input from the original instructions.
- Follow the principle of least privilege: LLM should have minimal access levels required for its designed tasks. Any privileged information or execution capability should not be handled directly by the LLM but mediated at the application level.
