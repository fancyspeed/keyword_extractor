#!/usr/bin/python
#coding: utf-8
# @author: zuotaoliu@126.com
# @created: 2014-06-23
import os
import sys
import math
sys.path.append('../')
import jieba
import jieba.posseg as pseg

class TextRankTagger(object):
    legal_pos_dict = {v:1 for v in ['a', 'an', 'i', 'j', 'l', 'n', 'nr', 'ns', 'nt', 'nz']}

    def __init__(self):
        jieba.initialize()
        jieba.enable_parallel(8)

    def tokenize(self, text):
        pos_list = pseg.cut(text)
        legal_list = []
        for v in pos_list:
            w, p = v.word, v.flag 
            if len(w)>1 and p in self.legal_pos_dict:
                legal_list.append(w.encode('utf-8'))
            else:
                legal_list.append('')
        return legal_list
        
    def get_und_unw_matrix(self, seg_list, window=4):
        # undirected and unweighted graph
        seg_matrix = {}
        for i, word in enumerate(seg_list):
            if not word: continue
            if word not in seg_matrix:
                seg_matrix[word] = set() 
            for k in range(1, window+1):
                j = i+k
                if j < len(seg_list):
                    word2 = seg_list[j]
                    if word2:
                        seg_matrix[word].add(word2)
                #j = i-k
                #if j >= 0:
                #    word2 = seg_list[j]
                #    if word2:
                #        seg_matrix[word].add(word2)
        return seg_matrix            

    def do_pagerank(self, matrix, w_dict, d=0.15):
        w_dict2 = {v:d for v in w_dict}
        for v in w_dict:
            if not matrix[v]: continue
            x = 1.0 / len(matrix[v])
            for v2 in matrix[v]:
                w_dict2[v2] += w_dict[v] * x * (1-d)
        for v in w_dict2:
            w_dict[v] = w_dict2[v]

    def get_topK(self, w_dict, K=5):
        sort_list = sorted(w_dict.items(), key=lambda d:d[1], reverse=True)
        return sort_list[:K]

    def abs_diff(self, old_words, new_words):
        diff = 0
        for i, pair in enumerate(old_words):
            w, v = pair
            if w == new_words[i][0]:
                diff += math.fabs(v - new_words[i][1])
            else: return 10000
        return diff

    def extract_keywords(self, text, n_count=5, window=4, d=0.15, max_iter=20):
        word_list = self.tokenize(text)
        matrix = self.get_und_unw_matrix(word_list, window)
        w_dict = {v:1.0 for v in matrix}
        old_top_words = self.get_topK(w_dict, n_count)

        for iter in xrange(max_iter):
            self.do_pagerank(matrix, w_dict, d)
            top_words = self.get_topK(w_dict, n_count)

            diff = self.abs_diff(old_top_words, top_words)
            if diff <= 0.00001: break
            old_top_words = top_words
        return self.get_topK(w_dict, n_count)

def test():
    tagger = TextRankTagger()
    lines = [
            '走到哪都是一个人的旅行，不过，我相信宁可没有不了迁就！我想走遍天涯海角，直到找到属于我的她，让我可以落叶归根！',
            '1949年10月1日，中华人民共和国成立了，全球1/4的人口得到解放，百分之八十的耕地都给予农民，十几亿农民得到了实惠，120%的力气发展生产。',
            '开发者可以指定自己自定义的词典，以便包含jieba词库里没有的词。虽然jieba有新词识别能力，但是自行添加新词可以保证更高的正确率',
            ]
    for text in lines:
        print text
        result = tagger.extract_keywords(text)
        for k, v in result: print k, v

if __name__ == '__main__':
    test()

