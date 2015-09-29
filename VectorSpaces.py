import logging
logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)
from gensim import corpora, models, similarities
documents = ["Human machine interface for lab abc computer applications","A survey of user opinion of computer system response time","The EPS user interface management system","System and human system engineering testing of EPS","Relation of user perceived response time to error measurement","The generation of random binary unordered trees","The intersection graph of paths in trees","Graph minors IV Widths of trees and well quasi ordering","Graph minors A survey"]

# remove common words and tokenize
stoplist = set('for a of the and to in'.split())
texts = [[word for word in document.lower().split() if word not in stoplist]
          for document in documents]

# remove words that appear only once
from collections import defaultdict
frequency = defaultdict(int)
for text in texts:
    for token in text:
        frequency[token] += 1

texts = [[token for token in text if frequency[token] > 1]for text in texts]

#The mapping between the questions and ids is called a dictionary:
dictionary = corpora.Dictionary(texts)
dictionary.save('/tmp/deerwester.dict')
print(dictionary)
print(dictionary.token2id)

#To actually convert tokenized documents to vectors:
new_doc = "Human computer interaction"
new_vec = dictionary.doc2bow(new_doc.lower().split())
print(new_vec)

#tener la representacion vectorial de los textos a partir del diccionario
corpus = [dictionary.doc2bow(text) for text in texts]
corpora.MmCorpus.serialize('/tmp/deerwester.mm', corpus) # store to disk, for later use
print(corpus)

#teniendo el corpus se puede relizar funciones estadisticas con corpora
