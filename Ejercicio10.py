#Escribir un programa que almacene en una lista los siguientes
#  precios, 50, 75, 46, 22, 80, 65, 8, y muestre por pantalla 
# el menor y el mayor de los precios.
lista = []
precios = ""
while precios != "no hay mas":
    precios = input("Dime el precio ")
    lista.append(precios)
lista.pop(len(lista) - 1)
lista.sort()
print(lista[0], "es el menor de todos")
print(lista[len(lista)-1], "es el mayor de todos")