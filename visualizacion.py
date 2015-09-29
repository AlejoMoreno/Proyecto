from __future__ import unicode_literals
from sklearn.decomposition import PCA
from sklearn.lda import LDA
from pysparse.sparse import spmatrix

import re
import matplotlib.pyplot as plt
import numpy as np
import nltk, sys


#Variables indicadores comparativos tag documents
archivo1 = sys.argv[1] #matriz dispersa matlab labels
archivo2 = sys.argv[2] #documentos labels
archivo3 = sys.argv[3] #tokens labels

archivo4 = sys.argv[4] #matriz dispersa matlab text
archivo5 = sys.argv[5] #documentos text
clase = sys.argv[6] #clase o etiqueta a buscar

matrizDispersa = np.loadtxt(archivo1, delimiter=",", dtype='str')
documents = np.loadtxt(archivo2, delimiter=",", dtype='str')
tokens = np.loadtxt(archivo3, delimiter=" ", dtype='str')
spmatrix.ll_mat_from_mtx(fileName)


#inicializacion de variables
arrayDocs = []
DocumentsGenerated = []

countD = 0
count = 0

#Encontrar los documentos que contienen la clase
for i in range(len(tokens)):
	if re.match(clase, tokens[i,0]):
		lineaClase = i

for i in range(len(matrizDispersa[0,:])): #terminos
	if i == lineaClase:
		for j in range(len(matrizDispersa[:,0])): #documentos
			countD = countD + 1
			if float(matrizDispersa[j,i])>0: #verificar si no es 0 en la matriz
				count = count + 1
				arrayDocs.append(j)

for i in range(len(documents)):
	for j in range(len(arrayDocs)):
		if i == arrayDocs[j]:
			DocumentsGenerated.append(documents[i])

#print DocumentsGenerated ARRAY QUE IDENTIFICA LOS DOCUMENTOS CONGRUENTES
print "Termino "+ clase + " se encuentra en la linea " + str(lineaClase+1)
print "Total documentos " + str(countD)
print "Documentos que contienen el termino "+str(clase)+" son: "+str(count)

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

#seccion PCA y normalizacion L1
matrizDispersa = np.loadtxt(archivo4, delimiter=",")
documents = np.loadtxt(archivo5, delimiter=",", dtype='str')

#"""normalizacion L1"""
normas = np.sum(matrizDispersa,axis=1)
normas.shape
matrizDispersa = (matrizDispersa.T*(1/normas)).T

#"""se realiza el pca de la matriz dispersa con 2 componentes"""
pca = PCA(n_components=2)
X_r = pca.fit(matrizDispersa).transform(matrizDispersa)

#visualizacion
for i in range(len(X_r[:,0])):
	for j in range(len(DocumentsGenerated)):
		if re.match(DocumentsGenerated[j].strip('tq'), documents[i].strip('q')):
			plt.text(X_r[i,0],X_r[i,1],'*',color='r',label = clase)
	plt.text(X_r[i,0],X_r[i,1],'.', label = "Other")

plt.title("Visualization "+clase+" in Post type text")
plt.legend(loc="upper left")  
plt.axis([min(X_r[:,0]), max(X_r[:,0]), min(X_r[:,1]), max(X_r[:,1])])
plt.show()

normas = N.sum(X,axis=1)
X = (X.T*(1/normas)).T
print 'Normalizacion X: ', N.sum(X,axis=1)

normas = N.sum(L,axis=1)
L = (L.T*(1/normas)).T
print 'Normalizacion L: ', N.sum(Y,axis=1)
