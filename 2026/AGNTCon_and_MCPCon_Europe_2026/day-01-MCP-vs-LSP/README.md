MCP Borrowed LSP's Design. It Skipped LSP's Lesson - Gorkem Ercan, Jozu

MCP borrowed its design from the Language Server Protocol. It skipped LSP’s hardest lesson, the one about packaging and trust, and a decade later that lesson is still unlearned.

LSP never standardized how servers were packaged or verified. Each editor invented its own channel, the VS Code extension format won by default, and signing was bolted on much later, marketplace by marketplace. It still has not closed the gap.

MCP repeats this with a larger blast radius. An MCP server runs arbitrary code that reaches into credentials, data, and local systems. Today’s packaging work falls short: the official registry delegates trust to npm and PyPI, the MCPB format repeats the VS Code extension model, and the provenance that exists is locked inside vendor silos.

What is missing is open, registry-neutral provenance verified before an agent loads a server. That standard does not need inventing. Packaging MCP servers as OCI artifacts inherits the signing, attestation, and policy tooling the container ecosystem already proved. This talk traces that history firsthand, then shows how to reuse it rather than rebuild it registry by registry.

Gorkem Ercan
CTO, Jozu

### Packaging / Standards

- KitOps (standards-based packaging & versioning for AI/ML projects): https://github.com/kitops-ml/kitops
- use with cosign
