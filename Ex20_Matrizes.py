"""
Faça um programa que gera uma Matrizes 8 x 8 onde :

a) os elementos das linhas pares são 1 e os elementos das linhas ímpares são 0.

b) os elementos da diagonal principal são 1 e os demais elementos são 0.

c) os elementos onde a soma de i + j for par são 1. Caso a soma seja impar o valor deve ser 0

d) gerar a matriz como:

0 1 0 1 0 1 0 1 

1 0 1 0 1 0 1 0 

0 1 0 1 0 1 0 1 

1 0 1 0 1 0 1 0 
0 1 0 1 0 1 0 1 

1 0 1 0 1 0 1 0 

0 1 0 1 0 1 0 1 

1 0 1 0 1 0 1 0 
"""

from random import randint
matriz = []
def MostrarMatriz(matriz):
    for linhas in matriz:
        print(linhas)
# Criar a matriz
for qlinhas in range(8):
    linhas = []
    for qcolunas in range(8):
        linhas.append(randint(0,9))
    matriz.append(linhas)
print("Matriz 8 x 8")
MostrarMatriz(matriz)
# item A
print("_"*20)
print("A - Elementos das linhas pares = 1 e impares = 0")
for qlinhas in range(8):
    for qcolunas in range(8):
        if qlinhas%2 == 0: # precisei inverter pq por algum motivo ele conta 8 vezes mas inicia pelo 0
            matriz[qlinhas][qcolunas] = 0
        else:
            matriz[qlinhas][qcolunas] = 1
MostrarMatriz(matriz)
# item B
print("_"*20)
print("B - Diagonal principal = 0")
for qlinhas in range(8):
    for qcolunas in range(8):
        if qlinhas + qcolunas == 7:
            matriz[qlinhas][qcolunas] = 0
        else:
            matriz[qlinhas][qcolunas] = 1
MostrarMatriz(matriz)
#item C
print("_"*20)
print("C - i+j par = 1, impar = 0")
for qlinhas in range(8):
    for qcolunas in range(8):
        if (qlinhas + qcolunas)%2 ==0:
            matriz[qlinhas][qcolunas] = 1
        else:
            matriz[qlinhas][qcolunas] = 0
MostrarMatriz(matriz)
# item D
print("_"*20)
print("D")
for qlinhas in range(8):
    for qcolunas in range(8):
        if (qlinhas + qcolunas)%2 ==0:
            matriz[qlinhas][qcolunas] = 0
        else:
            matriz[qlinhas][qcolunas] = 1
MostrarMatriz(matriz)
