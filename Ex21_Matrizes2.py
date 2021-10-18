"""
Exercícios
1 – Faça um programa que gere a matriz abaixo.
[2, 0, 0, 0, 0, 0, 0, 0]
[1, 2, 0, 0, 0, 0, 8, 0]
[1, 1, 2, 0, 0, 0, 0, 0]
[1, 1, 1, 2, 0, 0, 0, 0]
[1, 1, 1, 1, 2, 0, 0, 0]
[1, 1, 1, 1, 1, 2, 0, 0]
[1, 1, 1, 1, 1, 1, 2, 0]
[1, 1, 1, 1, 1, 1, 1, 2]
Depois de gerada essa matriz, gere a matriz transposta dela.
"""

matriz = []
qntlinhas = 8
qntcolunas = 8
for n in range(qntlinhas):
    linhas = []
    for n2 in range(qntcolunas):
        if n == n2:
            linhas.append(2)
        elif n == 1 and n2 == 6:
            linhas.append(8)
        elif n < n2:
            linhas.append(0)
        else:
            linhas.append(1)
    matriz.append(linhas)
for n in matriz:
    print(n)

matriz2 = []
for n in range(qntlinhas):
    linhas2 = []
    for n2 in range(qntcolunas):
        linhas2.append(matriz[n2][n])
    matriz2.append(linhas2)
print("_"*20)
print(" Matriz transposta")
for n in matriz2:
    print(n)

