"""
Um motorista de de taxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o preço do combustível é de R$3,50, escreva um programa em python para ler: 

- a marcação do odômetro no início do dia 

- a marcação no final do dia 

- o número de litros de combustível gasto 

- o valor total (R$) recebido dos passageiros. 

Calcule e escreva a média do consumo em Km/l e o lucro líquido do dia. Se o lucro líquido no dia for inferior a R$ 100,00 exiba a mensagem que o taxista precisa melhorar seu desempenho
"""

print("Olá, bem vindo")
mark1 = float(input("Digite a marcação do odometro no inicio do dia em quilometros"))
mark2 = float(input("Digite a marcação do odometro no final do dia em quilometros"))
v = int(input("Digite o valor total recebido pelos clientes no dia"))
co = float(input("Digite o consumo de combustivel gasto em litros"))
cam = mark2 - mark1
consumomedio = cam/co
print("Seu consumo medio foi de {:.2f}km por litro" .format(consumomedio))
lucroliquido = (v - (3.5*co))
print("O seu lucro liquido é de {} reais" .format(lucroliquido))
if lucroliquido < 100:
    print("Você precisa melhorar seu desempenho")
