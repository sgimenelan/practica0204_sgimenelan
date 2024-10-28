#Escribir un programa que almacene las asignaturas de un curso (por ejemplo Matemáticas,
#Física, Química, Historia y Lengua) en una lista y la muestre por pantalla el mensaje:
#Yo estudio <asignatura>, donde <asignatura> es cada una de las asignaturas de la lista.
lista = []
asignatura = ""
while asignatura != "no tengo mas":
    asignatura = input("Dime la asignatura: ")
    lista.append(asignatura)
lista.pop(len(lista) - 1)
for i in lista:
    print("Yo estudio", i)