from sklearn import datasets

# Problemas de clasificacion
iris = datasets.load_iris()        # Datos caracteristicas flor - iris
digits = datasets.load_digits()    # Datos clasificacion de digitos

diabetes = datasets.load_diabetes() # Datos Diabetes regresion

# datasets es un objeto tipo diccionario que contiene datos y metadatos
# .data -- Contiene los datos
# .data --> un array de componentes (n_samples, n_features)
# .target --> La verdad de lo que representa cada componente del array



print("Datos Iris -->")             
print(iris.feature_names)
print(iris.data[0:5])
print("Target Iris -->")       
print(iris.target)
print (len(iris))
for i in range(len(iris.data)):
    print(iris.target_names[iris.target[i]], iris.target[i])

print("Datos Digits -->")
print(digits.data[0:5])
print("Target Digits -->")
print(digits.target_names)
print(digits.target)

# print("Target - Digits -->")
# for i in range(5):
#     print(digits.target[i], digits.images[i])


# print("Datos Diabetes -->")
# print(diabetes.data[0:5])
# print("Target Diabetes -->")
# print(diabetes.target)
