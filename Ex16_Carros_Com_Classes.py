"""
Considere o cenário de um estacionamento que vende carros usados. Faça um programa para cadastrar e gerenciar os carros. Para cada carro deve ser cadastrado: modelo, ano de fabricação, preço, placa e status (LIVRE, RESERVADO, VENDIDO). Construa um menu onde é possível:

· Incluir novos carros. (incluir um carro por vez). O sistema não deve permitir o cadastro de dois carros com a mesma placa. Se isso ocorrer, o sistema deve informar ao usuário que não é possível cadastrar o carro.  Não deve ser permitido inserir carros com não maior que 2018 e menor que 1990 (dica: faça uma função que valide isso).

· Listar todos os dados dos carros cadastrados.

· Atualizar dados de um carro a partir de uma placa.

· Vender um carro: os sistema deve verificar se determinado carro (a partir de seu ano e modelo) está livre para venda. Se estiver, deve ser alterado o status para VENDIDO e computado a receita obtida pela venda.

· Listar o valor obtido por todas as vendas já realizadas.

· Buscar o valor total dos carros LIVRE, dos carros RESERVADO e dos que estão no status VENDIDO.

· Reservar um carro: o usuário digita a placa do carro e o sistema modifica a situação para RESERVADO caso ele esteja marcado como LIVRE. Se o carro estiver com a situação como VENDIDO, o programa deve dizer que o CARRO JÁ FOI VENDIDO. Se o status for RESERVADO, informar que o carro já está reservado.

· Exibir a quantidade de carros que tiveram seus dados atualizados.

· Exibir a quantidade de carros LIVRE com preço maior que R$ 50.000,00.

· Consulta para compra: o usuário deve informar o preço máximo que está disposto a pagar e o tempo máximo de uso do carro. O sistema deve trazer todos os possíveis carros que podem ser comprados.
"""

listadecarros = []
opcao = 7
vendattl = []
qntdeatualizacoes = []
soma = 0 # variavel para soma dos elementos da lista vendattl
soma2 = 0 # variavel para soma dos elementos da lista qntdeatualizacoes
from time import sleep

class Carro:
    def _unit_(self):
        self.modelo = ""
        self.ano = 0
        self.preco = 0.0
        self.placa = ""
        self.status = ""

def verificarplaca(lista, placax):
    nomeexiste = False
    for n in lista:
        if n.placa == placax:
            nomeexiste = True
    return nomeexiste


def verificarano(ano):
    anocorreto = False
    if ano > 1990 and ano < 2018:
        anocorreto = True
    return anocorreto

def menu():
    print("1 - cadastrar um carro:")
    print("2 - listar todos os carros:")
    print("3 - atualizar dados de um carro:")
    print("4 - vender um carro")
    print("5 - listar o valor obtido com todas vendas")
    print("6 - listar a quantidade carro de acordo com o status ")
    print("7 - reservar um carro")
    print("8 - exibir a quantidade de carros com dados atualizados")
    print("9 - a quantidade de carros livres com preco maior que 50mil")
    print("10 - Auxilio")
    print("0 - sair")

def verificarstatus(lista,placa):
    statuslivre = False
    for n in lista:
        if n.placa == placa and n.status == 1:
            statuslivre = True
    return statuslivre

def cadastrarcarros(lista):
    novocarro = Carro()
    novocarro.placa = input("Digite a placa do carro:")
    if verificarplaca(listadecarros, novocarro.placa) == False:
        novocarro.ano = int(input("Digite o ano do carro:"))
        if verificarano(novocarro.ano) == True:
            novocarro.modelo = input("Digite o modelo do carro:")
            novocarro.preco = float(input("Digite o valor do carro:"))
            novocarro.status = int(input("Digite o valor do status do carro( 1 - livre, 2 - reservado, 3 - vendido):"))
            listadecarros.append(novocarro)

        else:
            print("O ano digitado é invalido")
            sleep(2)
    else:
        print("A placa citada já existe")
        sleep(2)

def listarcarros(lista):
    print("Lista de carros")
    for n in lista:
        print(n.modelo)
        print("Placa:{}".format(n.placa))
        print("Preço:{}".format(n.preco))
        if n.status == 1:
            print("Status: Livre")
        elif n.status == 2:
            print("Status: Reservado")
        elif n.status == 3:
            print("Status: Vendido")
        print("Ano do carro: {}".format(n.ano))
        sleep(2)
def atualizarcarro(lista):
    placa = input("Digite a placa do carro o qual voce deseja atualizar")
    for n in lista:
        if n.placa == placa:
            ano = int(input("Digite o novo ano do carro"))
            if verificarano(ano) == True:
                preco = float(input("Digite o novo preço do carro"))
                modelo = input("Digite o novo modelo do carro")
                n.ano = ano
                n.preco = preco
                n.modelo = modelo
                qntdeatualizacoes.append(1)
            else:
                print("O o ano digitado é invalido")
        else:
            print("Não existe essa placa")
def vendercarro(lista):
    placa = input("Digite a placa do carro o qual voce deseja vender")
    if verificarplaca(listadecarros,placa) == True:
        if verificarstatus(listadecarros,placa) == True:
            for n in lista:
                if n.placa == placa:
                    n.status = 3
                    print("Venda realizada com sucesso")
                    vendattl.append(n.preco)
        else:
            print("Esse carro não está disponivel")
    else:
        print("Essa placa não existe")

def listarcarros2(lista):
    print("Carros livres:")
    for n in lista:
        if n.status == 1:
            print(n.modelo)
    print("Carros reservados:")
    for n in lista:
        if n.status == 2:
            print(n.modelo)
    print("Carros vendidos:")
    for n in lista:
        if n.status == 3:
            print(n.modelo)
def reservarcarros(lista):
    placa = input("Digite a placa do carro que voce deseja reservar")
    if verificarplaca(listadecarros,placa) == True and verificarstatus(listadecarros,placa) == True:
        for n in lista:
            if n.placa == placa:
                n.status = 2
        print("Reserva realizada com sucesso")
    elif verificarplaca(listadecarros,placa) == False:
        print("A placa digitada nao existe")
    elif verificarstatus(listadecarros,placa) == False:
        print("O carro está indisponivel")
while opcao != 0:
    menu()
    opcao = int(input("Digite a opcao desejada:"))
    if opcao == 1:
        cadastrarcarros(listadecarros)
    elif opcao == 2:
        listarcarros(listadecarros)
    elif opcao == 3:
        atualizarcarro(listadecarros)
    elif opcao == 4:
        vendercarro(listadecarros)
    elif opcao == 5:
        for n in vendattl:
            soma += n
        print("O valor obtido com todas vendas é {}".format(soma))
    elif opcao == 6:
        listarcarros2(listadecarros)
    elif opcao == 7:
        reservarcarros(listadecarros)
    elif opcao == 8:
        for n in qntdeatualizacoes:
            soma2 += n
        print("A quantidade de carros atualizados é {}".format(soma2))
    elif opcao == 9:
        soma3 = 0
        for n in listadecarros:
            if n.preco > 50000:
                soma3 += 1
        print("A quantidade de carros com valor maior que 50mil é {}" .format(soma3))

    elif opcao == 10:
        periodo = int(input("Digite ate o ano limite do carro que voce seja comprar"))
        preco = float(input("Digite o valor limite que voce deseja gastar:"))
        for n in listadecarros:
            if n.preco < preco:
                print(n.modelo)









