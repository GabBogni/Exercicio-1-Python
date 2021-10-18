"""
Faça um programa que gere números aleatórios entre 5 e 45 até gerar um número divisível por 7. Quando isso ocorrer informar:

-  a quantidade de números divisíveis por 4 e maiores que 30 que foram gerados

- a quantidade de números pares OU menores que 30 que foram gerados.

- o percentual de números pares e o percentual de números impares

- o maior número gerado
"""

loop = 0
x = 0
y = 0
t = 0
pares = 0
impares = 0
maior = 0
while loop == 0:
    from random import randint
    n = randint(5,45)
    print(n)
    t = t + 1
    if n%4 == 0 and n>30:
        x = x + 1
    if n%2 == 0:
        pares = pares + 1
    else:
        impares = impares + 1
    if n%2 == 0 or n<30:
        y = y + 1
    if n > maior:
        maior = n
    if n%7 ==0:
        loop = 1
print("A quantidade de numeros divisiveis por 4 e maiores que 30 gerados é {}" .format(x))
print("A quantidade de numeros pares ou menores que 30 gerados é {}" .format(y))
print("O maior numero gerado é {}" .format(maior))
porpares = pares * 100/t
porimpares = impares*100/t
print("A porcentagem de numeros pares em relacao ao total é {:.1f}%" .format(porpares))
print("A porcentagem de numeros impares em relacao ao total é {:.1f}%" .format(porimpares))

