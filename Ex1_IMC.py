"""
Faça um programa que leia a altura e o peso do indivíduo. Calcule o IMC do usuário ( IMC = peso / (altura*altura) ).

Depois, pergunte a ele qual faixa de IMC ele deseja ter, conhecendo as categorias e valores dos dados abaixo:

1 -abaixo do peso: abaixo de 18,5 

2 -peso normal: entre 18,5 e 25 

3 -acima do peso: entre 25 e 30 

4 -obeso: acima de 30

Por fim informe se o usuário precisa a quantidade de quilos que o usuário precisa ganhar ou perder para se enquadrar na faixa desejada
"""

print("Olá,Bem vindo")
peso = float(input("Digite seu peso"))
altura = float(input("Digite sua altura"))
IMC = peso / altura ** 2
print("Seu IMC é {:.1f}".format(IMC))
if IMC > 30:
    print(" Você está obeso")
else:
    if 30 >= IMC >= 25:
        print(" Você está acima do peso")
    else:
        if 18.5 <= IMC < 25:
            print(" Você está com o peso normal")
        else:
            if IMC < 18.5:
                print(" Você está abaixo do peso")
print("Tecle um x na frente da alternativa desejada ou pressione enter")
questao1 = str(input("Ficar obeso"))
questao2 = str(input("Ficar peso normal"))
questao3 = str(input("Ficar abaixo do peso"))
questao4 = str(input("Ficar acima do peso"))
if questao1 == "x" :
    print("Voce precisa engordar {:.1f} quilos" .format((30.1 * altura **2) - peso))
else:
    if questao2 == "x" and IMC < 18.5:
        print("Voce precisa engordar {:.1f} quilos".format((18.6 * altura **2) - peso))
    else:
        if questao2 == "x" and IMC >= 25:
            print("Voce precisa emagrecer {:.1f} quilos".format(peso - (24.9 * altura **2)))
        else:
            if questao3 =="x":
                print("Voce precisa emagrecer {:.1f} quilos".format(peso - (18.4 * altura **2)))
            else:
                if questao4 =="x":
                    print("Voce precisa engordar {:.1f} quilos" .format((25.1 * altura **2) - peso))