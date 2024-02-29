import pandas as pd
import numpy as np
from knn import KNN
from cnn import condensed_nearest_neighbors
import matplotlib.pyplot as plt

dataset = pd.read_excel(r"C:\Users\alber\OneDrive - INTEC\LAB MACHINE LEARNING\P2\knn_dataset.xlsx",sheet_name="Programming_exercise")
trainX = pd.read_excel(r"C:\Users\alber\OneDrive - INTEC\LAB MACHINE LEARNING\P2\knn_dataset.xlsx",sheet_name="Programming_exercise", usecols=[2,3,4])
trainY = pd.read_excel(r"C:\Users\alber\OneDrive - INTEC\LAB MACHINE LEARNING\P2\knn_dataset.xlsx",sheet_name="Programming_exercise", usecols=[1])
X_test = pd.read_excel(r"C:\Users\alber\OneDrive - INTEC\LAB MACHINE LEARNING\P2\knn_dataset.xlsx",sheet_name="Programming_exercise", usecols=[9,10,11])
Y_test = pd.read_excel(r"C:\Users\alber\OneDrive - INTEC\LAB MACHINE LEARNING\P2\knn_dataset.xlsx",sheet_name="Programming_exercise", usecols=[8])

trainX = np.array(trainX)
trainY = np.array(trainY)
X_test = np.array(X_test)
Y_test = np.array(Y_test)


S,S_labels = condensed_nearest_neighbors(trainX[1:,:],trainY[1:,:])
print(S.shape)
print(S_labels.shape)

# for i in range(S.shape[1]):
#     if S_labels[i]==1:
#         marcar = 'v'
#         color = 'red'
#     else:
#         marcar ='o'
#         color ='blue'
#     plt.scatter(x=S[0,i],y=S[1,i],c = color,s =100,marker = marcar)
# for j  in range(X_test.shape[1]):
#     plt.scatter(x=X_test[0,j],y=X_test[1,j],c = 'black',s =100,marker = 's')
    
# plt.xlabel('Peso (kg)')
# plt.ylabel('Estatura (m)')
# plt.title('Clasificador KNN')
# plt.legend()


X_test = X_test[1:20001,:]
print(X_test.shape)
Y_test = Y_test[1:20001,:]

clasificador = KNN(k=3)
clasificador.aprendizaje(S.transpose(),S_labels)
clasificar = clasificador.clasificacion(X_test.transpose())

print("Prediccion", clasificar)

def confusionmatrix(ytest, prediccion):

    # extract the different classes
    clase = np.unique(ytest)

    # initialize the confusion matrix
    matrix = np.zeros((len(clase), len(clase)))

    # loop across the different combinations of actual / predicted classes
    for i in range(len(clase)):
        for j in range(len(clase)):

           # count the number of instances in each combination of actual / predicted classes
           matrix[i, j] = np.sum((ytest == clase[i]) & (prediccion == clase[j]))

    return matrix

# def accuracy(confusion_matrix):
#     aciertos = np.sum(np.diag(confusion_matrix))
#     total = np.sum(confusion_matrix)
#     accuracy = aciertos / total
#     return accuracy

print("Y_test \n", Y_test.shape)
print("Clasificar \n", clasificar.shape)

cm = confusionmatrix(Y_test,clasificar)
# certeza = accuracy(cm)
print("Confusion matrix \n",cm)
# print("Acierto:", certeza)

#WHY DONT YOU WANNA WORK, WHAT ARE U MISSIIIIIIIIIIINGGGGGGG