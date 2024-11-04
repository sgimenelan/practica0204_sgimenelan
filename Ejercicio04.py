#Escribir un programa que pregunte al usuario los números
#ganadores de la lotería primitiva, los almacene en una 
#lista y los muestre por pantalla ordenados de menor a mayor.
lista = []
numero_ganador = ""
while len(lista) < 6:
    numero_ganador = input("Dime el numero: ")
    lista.append(numero_ganador)
lista.sort()
print(lista)

