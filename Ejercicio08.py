#Escribir un programa que pida al usuario una
#  palabra y muestre por pantalla si es un palíndromo.
palabra = input("Dime una palabra: ")
palabra_reversa = list(palabra)
palabra_reversa.reverse()
palabra = list(palabra)
if palabra == palabra_reversa:
    palabra = "".join(palabra)
    print(palabra, "es un palíndromo")
else:
    palabra = "".join(palabra)
    print(palabra, "no es un palíndromo")