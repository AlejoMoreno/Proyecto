import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim import corpora, models, similarities
corpus = [[(0, 1.0), (1, 1.0), (2, 1.0)],[(2, 1.0), (3, 1.0), (4, 1.0), (5, 1.0), (6, 1.0), (8, 1.0)],[(1, 1.0), (3, 1.0), (4, 1.0), (7, 1.0)],[(0, 1.0), (4, 2.0), (7, 1.0)],[(3, 1.0), (5, 1.0), (6, 1.0)], [(9, 1.0)],[(9, 1.0), (10, 1.0)],[(9, 1.0), (10, 1.0), (11, 1.0)],[(8, 1.0), (10, 1.0), (11, 1.0)]]
corpus
tfidf = models.TfidfModel(corpus)
vec = [(0, 1), (4, 1)]
print(tfidf[vec])
index = similarities.SparseMatrixSimilarity(tfidf[corpus], num_features=12)
sims = index[tfidf[vec]]
print(list(enumerate(sims)))
# donde 0 es el primer documento y 46% de acuracy[(0, 0.4662244), (1, 0.19139354), (2, 0.24600551), (3, 0.82094586), (4, 0.0), (5, 0.0), (6, 0.0), (7, 0.0), (8, 0.0)]

#luego de ello podemos usar similary.py 