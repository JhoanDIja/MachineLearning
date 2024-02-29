import numpy as np
from collections import Counter

class KNN:
    def __init__(self,k=3):
        self.k = k
    def aprendizaje(self,X,C):
        self.X =X # Matriz de vectores de caracteristicas
        self.c =C #clases asociadas a cada vector x(n)
        self.muestras = X.shape[1] #cantidad de muestras
    
    def clasificacion(self, Y):
        clases = []
        for i in range(Y.shape[1]):
            distancias = np.empty(self.muestras)
            for n in range(self.muestras):
                distancias[n] = EUCLIDEANA(self.X[:, n], Y[:, i])
            
            # Distancias más cercanas
            k_distancias = np.argsort(distancias)
            # Identificar las k distancias - clases
            k_etiquetas = self.c[k_distancias[:self.k]]
            # print(k_etiquetas)
            # Votación
            c = Counter(tuple(int(label) for label in k_etiquetas)).most_common(1)
            clases.append(c[0][0])  # Almacenamos la clase asignada al vector y(n)
        return clases
def EUCLIDEANA(x,y):
    return np.sqrt(np.sum((x-y)**2))