#Escribir un programa que almacene las matrices:
#A = 1   2   3  B =-1   0
#    4   5   6      0   1
#                   1   1
#en una lista y muestre por pantalla su producto.
A = [
    [1, 2, 3],
    [4, 5, 6,],
]
B = [
    [-1, 0],
    [0, 1],
    [1, 1],
]
resultado = [
    [0, 0,],
    [0, 0,],
]
"""for i in range(len(A)):
    for j in range(len(B)):
        for q in range(len(B[0])):
            resultado [i][q] = A[i][j] * B[j][q]"""
#Esta sin acabar
c11 = ((A[0][0] * B[0][0]) + (A[0][1] * B[1][0]) + (A[0][2] * B[2][0]))
c12 = ((A[0][0] * B[0][1]) + (A[0][1] * B[1][1]) + (A[0][2] * B[2][1]))
c13 = ((A[1][0] * B[0][0]) + (A[1][1] * B[1][0]) + (A[1][2] * B[2][0]))
c14 = ((A[1][0] * B[0][1]) + (A[1][1] * B[1][1]) + (A[1][2] * B[2][0]))
resultado = [
    [c11, c12,],
    [c13, c14,],
    ]
print(resultado)