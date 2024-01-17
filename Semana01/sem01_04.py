lista = [1,2,3,4,5,"hola",7,8,9,"adios"]
print("lista:", lista)
print("lista[0]=",lista[0],"lista[-1]=",lista[-1])
print("lista[1:3]=",lista[1:3],"lista[-4:-1]=",lista[-4:-1])

cuadrados = []
for numero in range(15):
    cuadrados.append(numero * numero)
print("Cuadrados:",cuadrados)

xalcuadrado = [x * x for x in range(15)]
print("'X' al cuadrado:",xalcuadrado)

texto = "Universidad Tecnologica de Chihuahua"
vocales = [letra for letra in texto if letra in 'aeiou']
print("vocales:",vocales)

def es_consonante(letra):
    vocales = 'aeiou'
    return letra.isalpha() and letra.lower() not in vocales

consonantes = [letra for letra in texto if es_consonante(letra)]
print("Consonantes:",consonantes)

numeros = [1.25, -9.45, 10.22, 3.78, -5.92, 1.16]
positivos = [cantidad if cantidad > 0 else 0.01 for cantidad in numeros]
print("positivos", positivos)

matriz = [[i for i in range(5)] for _ in range(6)]
print("Una matriz ",matriz)

matrizaplanada = [numero for renglon in matriz for numero in renglon]
print("La matriz aplanada ", matrizaplanada)


suma10 = sum([x for x in range(11)])
print("Suma de los primeros 10 numeros =", suma10)