# Living in your own bubble - Introduce DDD into legacy software

[Jacob Duijzer]

specification by example - BDD, Gherkin

- (extend, not modify)
- bubble context
- ACL (Anti-Corruption Layer)

- strangler pattern - run old and new in parallel and check for differences each day, slowly match to get zero diffs.

- ubiquitous language - use the same language as the domain experts (eg NL for dutch farmers).

- domain story telling - talk to stakeholders. make drawings of process as they talk, to see if understanding is correct. literally use their language (Dutch - dier not koe ...)

When not to use bubble context:
- if too much data to load
- if other processes are writing - then have sync issues - so would need full scale DDD

https://duijzer.com/talks/living-in-your-own-bubble/

The 'blue book' = Domain-Driven Design - by Erik Evans

- "GETTING DDD STARTED SURROUNDED BY LEGACY SYSTEMS" - [GETTING DDD STARTED SURROUNDED BY LEGACY SYSTEMS](./pdf/GettingStartedWithDDDWhenSurroundedByLegacySystemsV1.pdf) - https://www.domainlanguage.com/wp-content/uploads/2016/04/GettingStartedWithDDDWhenSurroundedByLegacySystemsV1.pdf

- https://www.dddcommunity.org/library/evans_2011_2/2

- see also [screenshots](./images/bubble-context/)
