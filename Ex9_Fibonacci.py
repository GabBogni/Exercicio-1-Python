"""
A série de Fibonacci é formada pela seqüência 0,1,1,2,3,5,8,13,21,34,55,... Faça um programa capaz de gerar a série até o n−ésimo termo. Ler o número n do usuário
"""

loop = int(input("Digite o n-ésimo termo da sequencia de Fibonacci que deseja ver"))
loop -= 2
v1 = 0
v2 = 1
print(v1)
print(v2)
while loop > 0:
    v3 = v1 + v2
    v1 = v2
    v2 = v3
    print(v3)
    loop -= 1