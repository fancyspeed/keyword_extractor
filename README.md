
## Algorithms for keyword extraction.

* tfidf\_rank

    *  features: TF, IDF (==1) 
    *  ranking: TF * IDF 

* text\_rank

    *  features: pos (for filtering), word neighbors 
    *  ranking: TextRank, which like PageRank, while building a relation matrix according to the words' positions.
    *  reference: http://www.cse.unt.edu/~rada/papers/mihalcea.emnlp04.pdf

* glm\_rank (TODO)

    *  features: word frequence (TF), word importance (IDF, Part-Of-Speech, Entity type), word position (such as whether both in title and body)
    *  ranking: train and predict by regression model.

* semantic\_rank (TODO)

    *  features: such as TF, IDF, POS, entity type ... 
    *  ranking: regression model plus SemanticRank, which like Pagerank, while building a relation matrix according to semantic similarity.
    *  re-ranking: document category based adjusting, task dependent word adjusting.

* topic\_rank (TODO)

    *  ranking: topic model, such as LDA.

##Requirements:

* jieba: chinese word segmenter, https://github.com/fxsjy/jieba

* word2vec: for building word similarities, https://code.google.com/p/word2vec/


