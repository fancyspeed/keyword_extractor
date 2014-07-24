
##Algorithms for keywork extractor.

* text\_rank

    *  like pagerank. Need to build a relation matrix according to the words' positions.

* simple\_rank

    *  word frequent (TF)
    *  word importance (IDF, POS)
    *  word position (both in title and body)
    *  task related word weight adjusting.

* semantic\_rank

    *  features used in simple\_rank
    *  build a relation matrix according to semantic similarity.

##Requirements:

* jieba: chinese word segmenter.

* word2vec: build word similarity.


