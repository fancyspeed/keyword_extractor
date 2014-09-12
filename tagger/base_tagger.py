#coding: utf-8

class BaseTagger(object):
    
    def __init__(self):
        pass

    def preprocess(self, doc):
        return doc

    def get_tokens(self, doc):
        # word, NER, phrase
        return []

    def aggregate_to_candidates(self, tokens):
        return []

    def get_base_scores(self, terms):
        # TF * Position_bias * IDF * NER_bias * term_type
        return []

    def rerank_by_candidate_relation(self, terms, relation_graph):
        # relation: adjust in doc, linguistic, semantic
        # reranking: pagerank
        return []

    def rerank_by_doc_category(self, terms, doc_category, category_terms):
        # reranking: score * p(term | class) * p(class | doc)
        return []

    def postprocess(self, terms):
        # score + task_depent_bias
        return []
