#Modelo matematico para predecir etiquetas a partir de un texto.
#Fredy Alejandro Moreno Castro

from sklearn.preprocessing import normalize
import matplotlib.pyplot as plt
import numpy as np
import nltk, sys
from scipy import linalg

#Variables de entorno
archivo1 = sys.argv[1] #matriz index texto esparcida (full)
archivo2 = sys.argv[2] #matriz index labels o etiquetas esparcida (full)

X = np.loadtxt(archivo1, delimiter=",", dtype='float')
L = np.loadtxt(archivo2, delimiter=",", dtype='float')
I = np.eye(X[0,:].size, dtype=int) #Identidad n x n
lamda = pow(10,-3)

#normalizacion L1
X = normalize(X, axis=1, norm='l1')
print 'Normalizacion X: ', np.sum(X,axis=1)

L = normalize(L, axis=1, norm='l1')
print 'Normalizacion L: ', np.sum(L,axis=1)

print 'La matriz X de tamanio (m x n)' , X.shape
print 'La matriz L de tamanio (m x l)' , L.shape
print 'La matriz Identidad de tamanio (n x n)' , I.shape
print 'Carga completa.'
print 'Lamda ' , lamda

#Ejecucion modelo matematico
# W = [(X.T*X) + lamda * Identidad]'-1 (X.T * L)

W = linalg.inv((X.T.dot(X))+lamda*I).dot(X.T.dot(L))

print '--------------------------------------------------------------------------------------'
print 'Modelo completo W es quien se encargara de proyectar las etiquetas para un post prueba'
print 'La Matriz W de tamanio (n x l)' , W.shape

#save matrix
np.savetxt('Wmodel.txt', W, delimiter=',')
print 'Matriz guardada con exito Wmodel.txt'
