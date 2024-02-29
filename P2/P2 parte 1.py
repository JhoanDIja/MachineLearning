import pandas as pd
import numpy as np
from knn import KNN
import matplotlib.pyplot as plt

handwritten_exercise_data = pd.read_excel(r"C:\Users\alber\OneDrive - INTEC\LAB MACHINE LEARNING\P2\knn_dataset.xlsx",sheet_name="Handwritten_exercise",usecols=[0,1,2,3,4,7,8,9,10])
# print(handwritten_exercise_data.head())

train_data = np.array(handwritten_exercise_data)
train_data1 = np.array(train_data[1:,2].reshape(15,1))
train_data2 = np.array(train_data[1:,3].reshape(15,1))
train_data3 = np.array(train_data[1:,4].reshape(15,1))
train_data = np.concatenate((train_data1,train_data2,train_data3),axis = 1).transpose()

genero = np.array(handwritten_exercise_data)
genero = genero[1:,1]
genero = np.uint8(genero)


nuevos_datos = np.array(handwritten_exercise_data)
nuevos_datos = nuevos_datos[1:4,5:8]
print("Shape de los nuevos datos",nuevos_datos.shape)

for i in range(train_data.shape[1]):
    if genero[i]==1:
        marcar = 'v'
        color = 'red'
    else:
        marcar ='o'
        color ='blue'
    plt.scatter(x=train_data[0,i],y=train_data[1,i],c = color,s =100,marker = marcar)
for j  in range(nuevos_datos.shape[1]):
    plt.scatter(x=nuevos_datos[0,j],y=nuevos_datos[1,j],c = 'black',s =100,marker = 's')
    
plt.xlabel('Peso (kg)')
plt.ylabel('Estatura (m)')
plt.title('Clasificador KNN')
plt.legend("Boys","Girls")

print("Train data shape \n ", train_data.shape)
print("genero shape \n", genero.shape)

clasificador =KNN(k=3)
clasificador.aprendizaje(train_data,genero)
clasificar = clasificador.clasificacion(nuevos_datos.transpose())
print('generos', clasificar)

# def confusionmatrix(ytest, prediccion):

#     # extract the different classes
#     clase = np.unique(ytest)

#     # initialize the confusion matrix
#     matrix = np.zeros((len(clase), len(clase)))

#     # loop across the different combinations of actual / predicted classes
#     for i in range(len(clase)):
#         for j in range(len(clase)):

#            # count the number of instances in each combination of actual / predicted classes
#            matrix[i, j] = np.sum((ytest == clase[i]) & (prediccion == clase[j]))

#     return matrix

# cm = confusionmatrix(genero,clasificar)
