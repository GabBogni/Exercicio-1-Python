"""
Faça um programa que gere randomicamente as operações matemáticas (soma, subtração, multiplicação e divisão) e os números que serão utilizados na operação. Depois de gerada a primeira operação, o programa deve perguntar para o usuário se ele deseja gerar mais uma operação. Enquanto ele responder Sim, uma nova operação (soma, subtração, multiplicação e divisão) deverá ser sorteada assim como os números para a operação. Gere os números entre 0 e 10 para fazer os cálculos. Quando o usuário responder que Não quer gerar mais uma operação, exibir quantas operações foram geradas no total e o percentual de operação de SOMA que foram geradas em comparação com as demais. DICA: para gerar qual operação matemática será executada, gere um número entre 1 e 4 e cada número corresponde a uma operação. 
"""
from random import randint
l = 0
qntop = 0
qntsoma = 0
while l == 0:
    n1 = (randint(0,10))
    n2 = (randint(0,10))
    o = (randint(1,4))
    qntop += 1
    if o == 1:
        r = n1 + n2
        s = str("+")
        qntsoma += 1
    else:
        if o == 2:
            r = n1 - n2
            s = str("-")
        else:
            if o == 3:
                r = n1 * n2
                s = str("*")
            else:
                if o == 4 and n2 != 0:
                    r = n1 /n2
                    s = str("/")

    if o == 4 and n2 == 0:
        print("f{n1}/0 = ? \f Ocorreu uma divisao por zero")
    else:
        print(f"{n1}{s}{n2} = {r:.2f}")
    re = str(input("Voce deseja realizar mais uma operação? \n -Sim(digite s) \n -Não(digite n)"))
    if re == "n":
        l += 1
psoma = qntsoma /qntop *100
print(f"Você realizou {qntop} operações matematicas")
print(f"A porcentagem de operações de soma em relacao ao total realizada é de {psoma}%")
print("ok, tenha um bom dia")

