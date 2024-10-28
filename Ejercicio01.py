#Escribir un programa que almacene las asignaturas de un curso 
#(por ejemplo Matemáticas, Física, Química, Historia y Lengua)
#en una lista y la muestre por pantalla.
lista = []
asignatura = ""
while asignatura != "no tengo mas":
    asignatura = input("Dime la asignatura: ")
    lista.append(asignatura)
numero = (len(lista) - 1)
print(lista[0:numero])
