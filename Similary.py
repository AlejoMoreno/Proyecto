from gensim import corpora, models, similarities
dictionary = corpora.Dictionary.load('/tmp/deerwester.dict')
corpus = corpora.MmCorpus('/tmp/deerwester.mm') # comes from the first tutorial, "From strings to vectors"
print(corpus)

#To follow Deerwester’s example, we first use this tiny corpus to define a 2-dimensional LSI space:
lsi = models.LsiModel(corpus, id2word=dictionary, num_topics=2)

#creacion de un nuevo documento para saber que tan similares son
doc = "Human computer interaction"
vec_bow = dictionary.doc2bow(doc.lower().split())
vec_lsi = lsi[vec_bow] # convert the query to LSI space
print(vec_lsi)

index = similarities.MatrixSimilarity(lsi[corpus]) # transform corpus to LSI space and index it
#save and load index 
index.save('/tmp/deerwester.index')
index = similarities.MatrixSimilarity.load('/tmp/deerwester.index')

#preparando algunos querys
sims = index[vec_lsi] # perform a similarity query against the corpus
print(list(enumerate(sims))) # print (document_number, document_similarity) 2-tuples

sims = sorted(enumerate(sims), key=lambda item: -item[1])
print(sims) # print sorted (document number, similarity score) 2-tuples

#[(2, 0.99844527), # The EPS user interface management system
#(0, 0.99809301), # Human machine interface for lab abc computer applications
#(3, 0.9865886), # System and human system engineering testing of EPS
#(1, 0.93748635), # A survey of user opinion of computer system response time
#(4, 0.90755945), # Relation of user perceived response time to error measurement
#(8, 0.050041795), # Graph minors A survey
#(7, -0.098794639), # Graph minors IV Widths of trees and well quasi ordering
#(6, -0.1063926), # The intersection graph of paths in trees
#(5, -0.12416792)] # The generation of random binary unordered trees