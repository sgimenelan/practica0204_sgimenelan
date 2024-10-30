#Escribir un programa que almacene las asignaturas de un curso (por ejemplo
#  Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte 
# al usuario la nota que ha sacado en cada asignatura y elimine de la lista
#  las asignaturas aprobadas. Al final el programa debe mostrar por pantalla 
# las asignaturas que el usuario tiene que repetir.
asignaturas = []
notas = []
asignatura = ""
while True:
    asignatura = input("Dime la asignatura: ")
    asignaturas.append(asignatura)
    if asignatura == "no tengo mas":
        break
    nota = float(input("Cuanto has sacado: "))
    notas.append(notas) 
    if nota >= 5:
        asignaturas.pop(len(asignaturas) - 1)
asignaturas.pop(len(asignaturas)-1)
print("Tienes que recuperar", asignaturas)

         

