import numpy as np

# Define the Euclidean distance function
def euclidean_distance(x1, x2):
    return np.sqrt(np.sum((x1 - x2) ** 2))

# Implement the Condensed Nearest Neighbors algorithm
def condensed_nearest_neighbors(X, y):
    S = [X[0]]  # Initialize the subset with the first instance
    S_labels = [y[0]]
    
    for i in range(1, len(X)):
        misclassified = True
        for j in range(len(S)):
            if S_labels[j] == y[i] and euclidean_distance(S[j], X[i]) == 0:
                misclassified = False
                break
        
        if misclassified:
            S.append(X[i])
            S_labels.append(y[i])
    
    return np.array(S), np.array(S_labels)


