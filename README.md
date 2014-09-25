
## Algorithms for keyword extraction.

* text\_rank

    *  features: pos (for filtering), word neighbors 
    *  ranking: TextRank, which like PageRank, while building a relation matrix according to the words' positions.
    *  reference: http://www.cse.unt.edu/~rada/papers/mihalcea.emnlp04.pdf

* glm\_rank (TODO)

    *  features: word frequence (TF), word importance (IDF, Part-Of-Speech, Entity category), word position (such as whether both in title and body)
    *  ranking: train and predict by linear/logistic regression

* semantic\_rank (TODO)

    *  features: including features used by simple\_rank
    *  ranking: glm\_rank plus SemanticRank, which like Pagerank, while building a relation matrix according to semantic similarity.
    *  re-ranking: doc category based adjusting, task related word weight adjusting.

* topic\_rank (TODO)

    *  ranking: topic model, such as LDA.

##Requirements:

* jieba: chinese word segmenter.

* word2vec: for building word similarities.


