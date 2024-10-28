#Escribir un programa que almacene las asignaturas de un curso 
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista y la muestre por pantalla.
numero = int(input("Dime el numero de asignaturas que tienes: "))
lista = []
for i in range(numero):
    lista.append(input("Dime la asignatura: "))
print(lista)
