"""
Faça um programa para informatizar um canil. Devem ser salvos os dados dos cachorros (nome, peso, raça, idade).

O programa deve permitir:

- cadastro de animais. Não deve ser permitido duplicidade no nome do cachorro;

- atualização dos dados do cachorros;

- encontrar o cachorro mais velho

- excluir os cachorros da raça “pitbull”

- encontrar o percentuais de cães que são vira-lata.

- encontrar o cachorro mais magro

- informar quantos cães existem de cada uma das raças.

 - considerando que o canil deve ter 2 quilos de ração para cada “quilo de cachorro” por mês, informar qual deve ser o estoque de ração para os próximos 12 meses.
"""

from time import sleep

opcao = 9
total = 0  # quantidade de cachorros
listadecachorros = []


class Cachorros:
    def _unit_(self):
        self.nome = ""
        self.raca = ""
        self.peso = 0.0
        self.idade = 0


def Menu():
    print("1- Cadastrar animal")
    print("2- Atualizar dados do animal")
    print("3- Encontrar cachorro mais velho")
    print("4- Excluir cachorros da raça pitbull")
    print("5- Encontrar percentual de vira-latas")
    print("6- Encontrar cachorro mais magro")
    print("7- Informar quantidade de cachorros por raça")
    print("8- Informar estoque de ração pela quantidade de animais no canil")


def VerificarNome(nome, lista):
    nomeexiste = False
    for n in lista:
        if n.nome == nome:
            nomeexiste = True
    return nomeexiste


def Cadastrar(lista):
    novocachorro = Cachorros()
    nome = input("Digite o nome do cachorro:")
    if VerificarNome(nome, listadecachorros) == False:
        novocachorro.raca = input("Digite a raça do cachorro:")
        novocachorro.peso = float(input("Digite o peso do cachorro:"))
        novocachorro.idade = int(input("Digite a idade do cachorro:"))
        novocachorro.nome = nome
        listadecachorros.append(novocachorro)
        global total
        total += 1
    else:
        print("O nome já existe")


def Listar(lista):
    for n in lista:
        print("_" * 20)
        print("NOME:" + n.nome)
        print("RAÇA:" + n.raca)
        print("IDADE:{}".format(n.idade))
        print("PESO:{}".format(n.peso))
        sleep(2)


def Atualizardados(lista):
    nome = input("Digite o nome do animal do qual deseja alterar os dados:")
    if VerificarNome(nome, listadecachorros) == True:
        for n in lista:
            if n.nome == nome:
                n.raca = input("Digite a raça do cachorro:")
                n.peso = float(input("Digite o peso do cachorro:"))
                n.idade = int(input("Digite a idade do cachorro:"))
    else:
        print("Esse nome não existe no sistema")


def Encontrarcachorromaisvelho(lista):
    maior = 0
    nome = ""
    for n in lista:
        if n.idade > maior:
            maior = n.idade
            nome = n.nome
    return nome


def Excluircachorros(lista):
    global total
    for n in lista:
        if n.raca == "pitbull" or n.raca == "Pitbull":
            lista.remove(n)
            total -= 1
            print("pitbull(s) removido(s) com sucesso")


def Encontrarpercentualviralatas(lista):
    qntdeviralatas = 0
    global total
    for n in lista:
        if n.raca == "vira-lata" or n.raca == "Vira-lata" or n.raca == "Viralata" or n.raca == "viralata":
            qntdeviralatas += 1
    percentual = qntdeviralatas / total * 100
    return percentual


def Encontrarcachorromaismagro(lista):
    menor = 999
    nome = ""
    for n in lista:
        if n.peso < menor:
            menor = n.peso
            nome = n.nome
    return nome


def InformarqntcachorrosporRaca(lista):
    listaderacas = []
    for n in lista:
        racaexiste = False
        for x in listaderacas:
            if n.raca == x:
                racaexiste = True
        if racaexiste == False:
            listaderacas.append(n.raca)
    for x in listaderacas:
        print("_" * 20)
        contador = 0
        for n in lista:
            if n.raca == x:
                contador += 1
        print("{}:{}".format(x, contador))


def Informarqntracao(lista):
    somapeso = 0
    for n in lista:
        somapeso += n.peso
    racaototal = somapeso * 24
    return racaototal


while opcao != 0:
    Menu()
    opcao = int(input("Digite a opção que voce deseja:"))
    if opcao == 1:
        Cadastrar(listadecachorros)
    elif opcao == 2:
        Atualizardados(listadecachorros)
    elif opcao == 3:
        print("O cachorro mais velho é {}".format(Encontrarcachorromaisvelho(listadecachorros)))
    elif opcao == 4:
        Excluircachorros(listadecachorros)
    elif opcao == 5:
        print("O percentual de vira-latas é {}".format(Encontrarpercentualviralatas(listadecachorros)))
    elif opcao == 6:
        print("O cachorro mais magro é {}".format(Encontrarcachorromaismagro(listadecachorros)))
    elif opcao == 7:
        InformarqntcachorrosporRaca(listadecachorros)
    elif opcao == 8:
        print("A quantidade de ração necessaria para 12 meses é {}kg".format(Informarqntracao(listadecachorros)))
    elif opcao == 10:
        Listar(listadecachorros)

