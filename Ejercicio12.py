#Escribir un programa que pregunte por una muestra de
#  números, separados por comas, los guarde en una lista
#  y muestre por pantalla su media y desviación típica.
import statistics
numeros = list(input("Dime unos numeros separados por comas: "))
while "," in numeros:
    numeros.remove(",")
numeros = list(map(float, numeros))
print("La media es: ", statistics.mean(numeros))
print("La desviacion tipica: ", statistics.stdev(numeros))
