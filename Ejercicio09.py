#Escribir un programa que pida al usuario una palabra 
# y muestre por pantalla el número de veces que 
# contiene cada vocal.
palabra = input("Dime una palabra:")
vocales = ["a","e","i","o","u"]
for i in vocales:
    print(i, "sale", palabra.count(i), "veces")