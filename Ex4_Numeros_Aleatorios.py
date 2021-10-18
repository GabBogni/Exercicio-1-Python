""" 
Faça um programa que gere números aleatórios entre 0 e 50 até o número 32 ser gerado. Quando isso ocorrer, informar: a. A soma de todos os números gerados b. A quantidade de números gerados que é impar c. O menor número gerado
"""

loop = 0
qntnumim = 0
somadosnum = 0
menorvalor = 50
while loop == 0:
    from random import randint
    n = (randint(0, 50))
    somadosnum = somadosnum + n
    print(n)
    if n <= menorvalor:
        menorvalor = n
    if n % 2 != 0:
        qntnumim = qntnumim + 1
    if n == 32:
        loop = 1
        print("Há {} numeros impares gerados".format(qntnumim))
        print("A soma dos numeros gerados é {}".format(somadosnum))
        print("O menor valor é {}".format(menorvalor))
