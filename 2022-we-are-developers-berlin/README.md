# WeAreDevelopers 2022 Berlin - README

## techs to try

### Data modeling and ETL and Data Pipelines

- [prisma](https://www.prisma.io/typescript) - TS ORM
- [singer.io](https://www.singer.io/) for building data pipelines (open source ETL) (OSS scripts to move data)

### Online paint tool

- [paint.js.org](https://paint.js.org/) (web hosted MS Paint)

- high perf CMS via [Contentful](https://www.contentful.com/pricing/) and [next.js](https://nextjs.org/)
  -- how to combine the GraphQL API of Contentful, a headless content management system (CMS), with Next.js's incremental static regeneration (ISR) feature in order to balance the advantages of high performance offered by static site generation with the ability for content editors to publish changes in no time.

### DSL (Language Modelling)

- [langium](https://github.com/langium/langium) - Langium: Design Your Own Language in Node.js and VS Code - (DSL built on Language Server Protocol which is used by VS Code)

### AI - Image Generation from Text

- [Jina](https://github.com/jina-ai/jina) - With a framework like Jina, searching cross-modal/multi-modal data via deep neural networks becomes extremely straightforward.
  -- [DALL&middot;E](https://openai.com/blog/dall-e/), a powerful image-to-text generator released by OpenAI in 2021
  -- [DALL&middot;E flow](https://github.com/jina-ai/dalle-flow/)
  -- _Cross-modal learning_ refers to any kind of learning that involves information obtained from more than one modality.
  -- _modality_ = Multimodal learning involves relating information from multiple sources.

## concepts

Trade-offs: can only optimize/guarantee for 2 of 3:

- CAP - Consistency, Availability, Partition-tolerance
- FAB - Fast, Accurate, Big-data _(but does CAP already cover this? depending on definitions...)_
