import numpy as np

# Distancia euclideana
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# Condensed nearest neighboor
def condensed_nearest_neighbors(Z, y):
    S = [Z[0]]  # Inicializando el subespacio S del espacio Z
    S_labels = [y[0]] #Clases del subespacio S
    
    #Aqui chequeamos si ya existe un punto en S el cual ya exista en el conjunto de datos Z
    for i in range(1, len(Z)):
        no_existe = True
        for j in range(len(S)):
            if S_labels[j] == y[i] and euclidean_distance(S[j], Z[i]) == 0:
                no_existe = False
                break
        
        if no_existe:
            S.append(Z[i])
            S_labels.append(y[i])
    
    return np.array(S), np.array(S_labels)


