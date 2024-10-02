import math as m

"""
#ejercicio 01
base = 15

altura = 10

areaRectangulo = base * altura

print(areaRectangulo)


#ejercicio 02



radio = float(input("Introduce el radio del círculo:  \n"))

areaCirculo = m.pi * m.pow(radio,2)

print("El área del círculo es: ", areaCirculo)

#ejercicio 03


a = float(input("introduzca un numero"))
b = float(input("introduzca otro numero"))

def relacion (a,b) : 
    if a > b:
        return 1
    
    if a < b:
        return -1
    
    if a == b:
        return 0

#ejercicio 04

a = 10
b = 5

def intermedio (a,b):
    return (a + b) / 2

print(intermedio(a,b))


#ejercicio 05

num = 15

min = 0

max = 10

def recortar (num , min ,max):
    
    if(num < min):
        return min
    if(num > max):
        return max
    else:
        return num
    

print (recortar(num,min,max))

"""""
#ejercicio 06


numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def separar(lista):
    pares = []
    impares = []
    for i in lista:
        if i % 2 == 0:
            pares.append(i)
        else:
            impares.append(i)
    pares.sort()
    impares.sort()
    return pares, impares

pares, impares = separar(numeros)
print("Pares:", pares)
print("Impares:", impares)
