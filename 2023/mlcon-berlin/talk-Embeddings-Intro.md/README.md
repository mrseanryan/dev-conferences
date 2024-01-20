# Embeddings Intro - Christoph-Henkelmann

Intro to embedding vectors.

embeddings
- do use SBert (word2vec glove)
- do NOT use openai embeddings - inefficient and not very good

- use resnext one layer before output. then cluster
- can classify images!

dot prod of 2 normalised vectors = cos Angle
cosine distance = 1 - v.w
smaller then closer

more accurate:
- take several embeddings per class and use their average for that class

- try different embeddings, can get better results
- try different distance measures from your library

- use a threshold: if distance > X then is Unknown

- autoencoders are hard to use!
- use if lot of unlabelled data
- bigger layers getting smaller and smaller then bottleneck layer then more growing layers
- have an inner bottleneck layer that forces classification
- throw away decoder layers
then can train a classification layer with small number of labelled data

use postgres as a vector db - the embedding is the index
or if small data just in memory on the gpu
