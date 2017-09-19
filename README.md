
## Algorithms for keyword (tag) extraction.

* tf\_idf\_rank

    *  features: TF, IDF, pos-tagging
    *  filtering: by pos-tagging (such adj, conj...) 
    *  ranking: TF * IDF 

* text\_rank

    *  features: word neighbors 
    *  filtering: by pos-tagging (such adj, conj...) 
    *  ranking: TextRank, which like PageRank, while building a relation matrix according to the words' positions.
    *  reference: http://www.cse.unt.edu/~rada/papers/mihalcea.emnlp04.pdf

* glm\_rank (TODO)

    *  features: TF, IDF, pos-tagging, entity type, word position
    *  ranking: train and predict by classification model

* semantic\_rank (TODO)

    *  features: such as TF, IDF, POS, entity type ... 
    *  first-ranking: classification model
    *  re-ranking: adjust based on word co-occurence (Kobe and Oneal support each other)  or topic model (whether words are belongs the main topics)


##Requirements:

* jieba: chinese word segmenter, https://github.com/fxsjy/jieba

* word2vec: for building word similarities, https://code.google.com/p/word2vec/


