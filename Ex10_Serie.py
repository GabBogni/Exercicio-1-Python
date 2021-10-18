"""
Elabore um programa que mostre os n termos da Série a seguir: 

 S = 1/1 - 3/5 + 6/10 - 9/15 + 12/20 -  15/25... + n/m. 

Imprima no final a soma da série. Leia o valor de (n)
"""

loop = int(input("Digite o n-ésimo termo da sequencia especifica"))
loop -= 1
v1 = 1
v2 = 1
n = 0
sinal = +1
n2 = 1
soma = 0
print("n1 =(1/1) = 1")
while loop > 0:
    n += 1
    n2 += 1
    sinal *= -1
    v1 = 3*n
    v2 = 5*n
    v3 = (v1/v2)*sinal
    print(f"n{n2} = {sinal}*({v1}/{v2}) = {v3}")
    soma += v3
    loop -= 1
print("_"*20)
print(f"O n-ésimo termo da sequencia especifica é {sinal}*{v1}/{v2}")
print("A soma até o n-ésimo termo da sequencia especifica é {}" .format(soma + 1))