"""
Faça um programa para informatizar o cadastro de produtos em uma loja. Você deve cadastrar produtos até o preço 0 ser cadastrado. Cada produto deve ser armazenado com as seguintes informações: nome, preço, quantidade e categoria (“L” para luxo e “C” para comum). Depois de cadastrados os animais informe:

- a quantidade de produtos de luxo com preço menos de R$ 2000,00

- o preço médios dos produtos de luxo

- o nome do produto mais caro com quantidade menos que 50.

- o percentual de produtos que custam entre R$ 100,0 e R$ 200,00.
- o nome do produto comum mais barato
"""

loop = 0
q1 = 0
q2 = 0
q3 = 0
s1 = 0
qt = 0
mv = 0
novonome = "nenhum"
novonome2 = "nenhum"
mnv = 99999999999999999999999999999999999999999999999999
while loop == 0:
    p = float(input("Digite o valor do produto"))
    if p == 0:
       break
    c = str(input("Digite a categoria do produto: C ou L"))
    q = int(input("Digite a quantidade de produto"))
    n = str(input("Digite o nome do produto"))
    print("_" * 30)
    qt += q
    if p < 2000 and c == "L":
        q1 += q
    if c == "L":
        s1 += p
        q2 += 1
    if p > mv and q < 50:
        mv = p
        novonome = n
    if p < 200 and p > 100:
        q3 += q
    if c == "C" and p < mnv:
        mnv = p
        novonome2 = n
if q2 != 0:
    pm = s1 / q2
else:
    pm = 0
if qt != 0:
    p1 = q3 / qt * 100
else:
    p1 = 0
print(f"a quantidade de produtos de luxo com preço menor de R$ 2000,00 é {q1}")
print(f"o preço médios dos produtos de luxo é {pm}")
print(f"o nome do produto mais caro com quantidade menor que 50 é {novonome}")
print(f"o percentual de produtos que custam entre R$ 100,0 e R$ 200,00 é {p1}")
print(f" o nome do produto comum mais barato é {novonome2}")

#erros e correcoes durante o exercicio:
# *atencao na variavel quantidade
