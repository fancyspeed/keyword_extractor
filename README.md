
## Algorithms for keyword extraction.

* text\_rank

    *  like PageRank. Need to build a relation matrix according to the words' positions.
    *  http://www.cse.unt.edu/~rada/papers/mihalcea.emnlp04.pdf

* simple\_rank

    *  word frequence (TF)
    *  word importance (IDF, Part-Of-Speech)
    *  word position factor (such as whether both in title and body)
    *  task related word weight adjusting.

* semantic\_rank

    *  including features used by simple\_rank
    *  build a relation matrix according to semantic similarity.

##Requirements:

* jieba: chinese word segmenter.

* word2vec: for building word similarities.


