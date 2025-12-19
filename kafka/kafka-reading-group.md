# kafka reading notes

## the book

## Kafka: The Definitive Guide. Real-Time Data and Stream Processing at Scale

http://shop.oreilly.com/product/0636920044123.do

"you'll learn Kafka's design principles, reliability guarantees, key APIs, and architecture details, including the replication protocol, the controller, and the storage layer."

https://www.confluent.io/wp-content/uploads/confluent-kafka-definitive-guide-complete.pdf

## rough notes

# 1

kafka - its OK to store data there long-term:
https://www.confluent.io/blog/okay-store-data-apache-kafka/

zalando - a distributed event ust with a RESTful API
abstraction on top of kafka-like Qs (but kafka is not just Qs...)
https://github.com/zalando/nakadi

datomic - append-only/immutable database:
https://docs.datomic.com/on-prem/overview.html

# 2

Want guaranteed ordering
Then 1 partition in the topic
But then can it still scale?

* what is repn factor
* what happens if shut down not clean p 23

Zookeeper is critical p 38
Zookeeper ensemble is a cluster?

Partition key is domain dependent
Else msgss not sorted on consume
e.g.
Oil data:
oil rig id

Or mobile topups:
merchant group id

Could patch by creating a derived stream
But not efficient as writers keep writing to the original streams

Zookeeper voting algorithm
ZAB
2 variants
Has additional guarantee of ordering of config events that paxos does not give

# 3

* p50 batch size why not msg cnt and Kafka figures it out?
* p 52 ordering guarantees - need calc partitions upfront!?
  and retries with mult partitions can disrupt order ...
  So in practice ordering only guaranteed in ltd circumstances...
* p58 schema code for generics is manky!

Ordering:
Setting up keys to write to partition should fix Ordering?
But what about retries?

For ordering within partition with retries:
Need set:
max in flight req per session = 1

# 4

Partitioning defined in client seems bad
Example: schema registry for schemas so is centralised
But they don't centralise partitioning!
So hard to change partition

---

Ordering
LinkedIn didn't care much about ordering
So neither does kafka!?

Could partition keys be set in zookeeper and clients read that to decide partition ?

max topics 30,000 topics per cluster

Kafka - how find offset for a time?

Kafka can get the file with timestamp before that time
So you get earlier data

# 5 - blog posts about exactly-once + transactions

https://www.confluent.io/blog/exactly-once-semantics-are-possible-heres-how-apache-kafka-does-it/

https://www.confluent.io/blog/transactions-apache-kafka/

(see blogs folder)

Kafka consumers p82 and p85

# 6 serde

Serializers: Avro (used with kafka), Protobuf, Thrift, (JSON)

# 6b kafka - for transport not as an event source

https://medium.com/serialized-io/apache-kafka-is-not-for-event-sourcing-81735c3cf5c

use this instead:

serialized.io
https://serialized.io/

#7 kafka alternative

kafka alternative - AxonDB - high-performance event store

AxonDB – high-performance event store
https://www.youtube.com/watch?v=H20hh5oXzrk

#8 blogs

## Event First Development - Moving Towards Kafka Pipeline Applications

https://jobs.zalando.com/tech/blog/event-first-development---moving-towards-kafka-pipeline-applications/

## hosting

### kafka on AWS

as service:
https://aws.amazon.com/quickstart/architecture/confluent-platform/

hosting on aws EC2:
https://aws.amazon.com/blogs/big-data/best-practices-for-running-apache-kafka-on-aws/?utm_campaign=crowdfire&utm_content=crowdfire&utm_medium=social&utm_source=twitter

### kafka on Google Cloud

https://cloud.google.com/blog/big-data/2018/05/google-cloud-platform-and-confluent-partner-to-deliver-a-managed-apache-kafka-service

### kafka best practices (a summary)

https://community.hortonworks.com/articles/80813/kafka-best-practices-1.html

## monitoring

### chaperone - How Uber audits kafka

https://eng.uber.com/chaperone/
