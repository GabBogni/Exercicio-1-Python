"""
Faça um programa para informatizar o cadastro dos alunos em uma escola. Você deve cadastrar os alunos com as seguintes informações: nome, idade, sexo (M ou F) e peso. Devem ser cadastrados alunos até que a idade seja 0 (zero). Depois de cadastrados os alunos, informe:

- peso médio dos alunos do sexo masculino com mais de 10 anos.

- o percentual de alunos (masculino ou feminino) que pesam entre 35 e 45 quilos.

- o nome do aluno (ou aluna) com menor peso e com idade menor 10 anos.

- o nome da aluna (do sexo feminino) mais velha.

- a quantidade de alunos (do sexo masculino) ou com idade maior que 15 anos.
"""

sp1 = 0
qt1 = 0
qt2 = 0
qt3 = 0
qtt = 0
n3 = "nenhum"
n2 = "nenhum"
menorp = 999999999
maiori = 0
i = 1
while i > 0:
    i = int(input("Digite a idade do aluno"))
    if i == 0:
        break
    n = str(input("Digite o nome do aluno"))
    s = str(input("Digite o sexo do aluno: M ou F"))
    p = float(input("Digite o peso do aluno"))
    qtt += 1
    print("_"*30)
    if i > 10 and s == "M":
        sp1 += p
        qt1 += 1
    if p > 35 and p < 45:
        qt2 += 1
    if i < 10 and p < menorp:
        menorp = p
        n2 = n
    if i > maiori and s == "F":
        maiori = i
        n3 = n
    if s == "M" and i > 15:
        qt3 += 1
if qt1 > 0:
    pm = sp1 / qt1
else:
    pm = 0
if qtt > 0:
    por = qt2 /qtt * 100
else:
    por = 0
print(f"O peso médio dos alunos do sexo masculino com mais de 10 anos é {pm}")
print(f"O percentual de alunos que pesam entre 35 e 45 é {por}")
print(f"O  nome do aluno com menor peso e com idade menor que 10 anos é {n2}")
print(f"O nome da aluna mais velha é {n3}")
print(f"A quantidade de alunos do sexo masculino com idade maior que 15 anos é {qt3}")

#erros e correcoes durante o processo:
#divisao por zero na media e porcentagem qnd n há o denominador
#o loop parar antes de contar dados de qnd idade for 0 pelo comando break
# definir um valor no inicio para a variavel nome de menor ou maior valor para o caso de nao existir dentro das condicoes , fazendo ele procurar um variavel n definida
# correcao na logica da procura do nome no maior e menor


