import nltk, sys
import numpy as N
from nltk.corpus import PlaintextCorpusReader
from scipy import sparse
import re

import matplotlib.pyplot as plt
from scipy import linalg
import random

archivo1 = sys.argv[1] #archivo Ttokens
archivo2 = sys.argv[2] #matriz imagen espacial W
archivo3 = sys.argv[3] #archivo Ltokens
archivo4 = sys.argv[4] #new post
Ttokens = N.loadtxt(archivo1, delimiter=",", dtype='str')
Ltokens = N.loadtxt(archivo3,delimiter=",", dtype='str')
stopwordList = nltk.corpus.stopwords.words('english')
porter = nltk.PorterStemmer()
docCollection = PlaintextCorpusReader(archivo4, '.*')

# purify text(delete stopwords and write the porter (raiz))
actualWords = set(w.lower() for w in docCollection.words() if w.isalpha())
textVocab = set(w for w in actualWords if w not in stopwordList)
normWords = list(set(porter.stem(t) for t in textVocab))
print len(normWords),' after steamming'

#dictionary words new post
normWords.sort()
dict = {}
for w in normWords:
  dict[w] = normWords.count(w)

# TF-IDF execution
MFtd=dict.items()[N.argmax(dict.values())][1]
vectorX=N.zeros(len(Ttokens))
##implementacion TF
for w in range(len(Ttokens)):
  for j in normWords:
    if Ttokens[w].split()[0] == j:
      Ftd = dict[j]
      TF = 0.5+((0.5*Ftd)/MFtd)
      IDF = N.log(18211/(float(Ttokens[w].split()[2])+1))
      print 'posicion: '+ str(w) +' palabra: '+ j +' cantidad: '+ str(dict[j])+' TF: '+str(TF)+' IDF:'+str(IDF)
      vectorX[w]=(TF*IDF)

#normalize L1
x = normalize(vectorX, axis=1, norm='l1')
print 'Normalizacion X: ', N.sum(x,axis=1)

#Predicction label
W = N.loadtxt(archivo2,delimiter=",", dtype='float')
labels = x.dot(W) # visualizacion de los labels a traves de W
print 'La matriz labels resultante ' , labels.shape
print 'Primeros 5 indices : '
Plabel = N.argsort(labels, key=lambda X: X[1], reverse=True)

#visualizacion etiquetas resultantes
for i in N.argsort(labels)[0:4]:
  lista.append(tokens[i].split()[0])
print lista
return lista

Problema en Tokens labels

