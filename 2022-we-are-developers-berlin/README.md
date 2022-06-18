# WeAreDevelopers 2022 Berlin - README

## techs to try

### Data modeling and ETL and Data Pipelines

- [prisma](https://www.prisma.io/typescript) - TypeScript ORM
- [singer.io](https://www.singer.io/) for building data pipelines (open source ETL) (OSS scripts to move data)

### High perf CMS

- high perf CMS via [Contentful](https://www.contentful.com/pricing/) and [next.js](https://nextjs.org/)

  -- how to combine the GraphQL API of Contentful, a headless content management system (CMS), with Next.js's incremental static regeneration (ISR) feature in order to balance the advantages of high performance offered by static site generation with the ability for content editors to publish changes in no time.

### DSL (Language Modelling)

- [langium](https://github.com/langium/langium) - Langium: Design Your Own Language in Node.js and VS Code - (DSL built on Language Server Protocol which is used by VS Code)

### AI - Image Generation from Text

- [Jina](https://github.com/jina-ai/jina) - With a framework like Jina, searching cross-modal/multi-modal data via deep neural networks becomes extremely straightforward.

  -- [DALL&middot;E](https://openai.com/blog/dall-e/), a powerful image-to-text generator released by OpenAI in 2021

  -- [DALL&middot;E flow](https://github.com/jina-ai/dalle-flow/)

- [terminusDB](https://github.com/terminusdb/terminusdb) - modular toolkit for data intensive apps — OSS! - [organisation site](https://terminusdb.com)

---

### AI NLP

_presenter: [Jonas Andrulis](https://de.linkedin.com/in/jonasandrulis)_

- classical NLP - BM25

- transformers instead, vector compute and compare
- [ms marco](https://microsoft.github.io/msmarco/) - a collection of datasets focused on deep learning in search.
- [hugging face](https://huggingface.co/) - ML images
- [sbert.net](https://sbert.net/) - (via Niels Reimers) - sentence transformers.

combine classical and modern NLP (as they have complimentary strengths & weaknesses) (via voting?)

[vespa.ai](https://vespa.ai/) - [OSS](https://github.com/vespa-engine) tool, platform to build big data services

- [world models](https://worldmodels.github.io/)

-- world models don’t need labelled data

-- trained with lots of data - images or game screenshots/video

-- AI learns to predict whats next

-- LLMs trained on all human text! - _Logic learning machine (LLM) is a machine learning method based on the generation of intelligible rules._

---

## tools

- [deckset](https://www.deckset.com/) - app to create PowerPoint like slides from md (markdown) files

- [elastic search](https://www.elastic.co/) - can use via browser console

- [paint.js.org](https://paint.js.org/) (web hosted MS Paint)

---

## platforms

[eyeson](https://eyeson-team.github.io/api/getting-started/) - API for meeting management & control + video

[neon](https://neon.tech/) - serverless postgres. with free tier

[codeanywhere](https://codeanywhere.com/) - cloud code env

[solace.com](https://www.solace.dev/) - events platform - integrate with mx?? mx uses kafka directly but thats complex and then coupled…

-- sources: kafka, mqtt and iot (smart things like smart lamp, lights...)

---

## books

[clean architecture](https://www.amazon.nl/Clean-Architecture-Craftsmans-Software-Structure/dp/0134494164/ref=asc_df_0134494164/) - uncle bob

tech design - “??High design”.

[domain driven design](https://www.bol.com/nl/nl/p/domain-driven-design/1001004001984629/) - erik evans

-- _page 140: strategic design_
event storming
domain story telling

domain (business) gives bounded ctxts. THEN can design events between the ctxts.

[documenting software architecture](https://www.amazon.nl/Documenting-Software-Architectures-Views-Beyond/dp/0321552687/ref=asc_df_0321552687/)

[sustainable software architecture](https://sustainable-software-architecture.com/)

---

## concepts

Trade-offs: can only optimize/guarantee for 2 of 3:

- CAP - Consistency, Availability, Partition-tolerance
- FAB - Fast, Accurate, Big-data _(but does CAP already cover this? depending on definitions...)_

- _modality_ = Multimodal learning involves relating information from multiple sources.

- _Cross-modal learning_ refers to any kind of learning that involves information obtained from more than one modality.
