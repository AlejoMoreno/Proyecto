import nltk, sys
import numpy as N
from nltk.corpus import PlaintextCorpusReader
from scipy import sparse
import re

import matplotlib.pyplot as plt
from scipy import linalg
import random

archivo4 = sys.argv[4] #new post

stopwordList = nltk.corpus.stopwords.words('english')
porter = nltk.PorterStemmer()
docCollection = PlaintextCorpusReader(archivo4, '.*')

# purify text(delete stopwords and write the porter (raiz))
actualWords = set(w.lower() for w in docCollection.words() if w.isalpha())
textVocab = set(w for w in actualWords if w not in stopwordList)
normWords = list(set(porter.stem(t) for t in textVocab))
print len(normWords),' after steamming'

