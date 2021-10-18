"""
Um vendedor de carros recebe comissão de 10% a cada carro vendido com o valor até R$10.000,00 e comissão de 11% sobre os carros vendidos que custem mais R$10.000,00. Faça um programa que leia do vendedor a quantidade de carros que o ele vendeu. Depois, para cada carro vendido leia o valor do carro e a modelo do carro. No fim exiba: 

a. Quanto o vendedor receberá de comissão. 

b. O modelo do carro mais caro. 

c. A quantidade de carros que custam mais que R$20.000,00 e menos que R$30.000,00. 

d. O preço médio dos carros.
"""

maiorv = 0
lucrot = 0
nx = 0
somavalor = 0
ncarros = 0
qntdeloops = int(input("Digite a quantidade carros vendidos"))
while qntdeloops != 0:
    print("___________________________________________")
    valor = float(input("Digite o valor do carro"))
    modelo = str(input("Digite o modelo do carro"))
    print("____________________________________________")
    qntdeloops -= 1
    somavalor += valor
    ncarros += 1
    if valor < 10000:
        lucrot += valor/100 * 10
    else:
        lucrot += valor/100 * 11
        # igual tambem está contando
    if valor > maiorv:
        maiorv = valor
        modelomaiscaro = modelo
    if valor > 20000 and valor < 30000:
        nx +=1
valorm = somavalor / ncarros
print("O valor recebido por todos carros é R${}" .format(lucrot))
print("O carro mais caro custa R${}, sendo do modelo{}".format(maiorv,modelomaiscaro))
print("Existem {} carros que custam mais do que 20mil e menos do que 30mil" .format(nx))
print("O valor medio dos carros é R${}" .format(valorm))

