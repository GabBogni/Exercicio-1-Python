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

placas=[]
precos=[]
anos=[]
modelos=[]
status=[]
opcao = 7
somavendas = 0
qntcarrosatualizados = 0
def verificarplaca(placas,placaregistrada):
    existe = False
    for n in placas:
        if n == placaregistrada:
            existe = True
    return existe
def verificarano(anocadastrado):
    dentrodoperiodo = False
    if anocadastrado > 1990 and anocadastrado < 2018:
        dentrodoperiodo = True
    return dentrodoperiodo

while opcao != 0:
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
    opcao = int(input("Digite a opcao desejada:"))
    if opcao == 1:
        iplaca = input("Digite a placa do carro que voce deseja registrar:")
        if verificarplaca(placas,iplaca) == False:
            iano = int(input("Digite o ano do carro:"))
            if verificarano(iano) == True:
                imodelo = input("Digite o modelo do carro:")
                istatus = int(input("Digite o status do carro: 1 - vendido, 2 - reservado, 3 -livre:"))
                ipreco = float(input("Digite o preço do carro:"))
                placas.append(iplaca)
                precos.append(ipreco)
                anos.append(iano)
                modelos.append(imodelo)
                status.append(istatus)
                print("Registro realizado com sucesso")
            else:
                print("o ano digitado está fora do intervalo aceitavel")
        else:
            print("A placa digitada já existe")
    else:
        if opcao == 2:
            indice = 0
            for n in modelos:
                print("_"*50)
                print(n)
                indice += 1
        else:
            if opcao == 3:
                iplaca = input("Digite o nome da placa que voce deseja alterar os dados")
                if verificarplaca(placas,iplaca) == True:
                    indice = 0
                    for n in placas:
                        if n == iplaca:
                            iano = int(input("Digite o novo ano do carro:"))
                            if verificarano(iano) == True:
                                imodelo = input("Digite o novo modelo do carro:")
                                ipreco = float(input("Digite o novo preço do carro:"))
                                precos[indice] = ipreco
                                anos[indice] = iano
                                modelos[indice] = imodelo
                                qntcarrosatualizados += 1
                                print("alteração de dados feita com sucesso")
                            else:
                                print("ano digitado invalido")
                        indice += 1
                else:
                    print("nome da placa nao existente")
            else:
                if opcao == 4:
                    iplaca = input("Digite a placa do veiculo que voce deseja vender:")
                    if verificarplaca(placas,iplaca) == True:
                        indice = 0
                        carrovendido = False
                        carroreservado = False
                        for n in placas:
                            if n == iplaca and status[indice] == 3:
                                status[indice] = 1
                                somavendas += precos[indice]
                            elif n == iplaca and status[indice] == 1:
                                carrovendido = True
                            elif n == iplaca and status[indice] == 2:
                                carroreservado = True
                            indice += 1
                        if carrovendido == True:
                            print("este carro ja foi vendido")
                        if carroreservado == True:
                            print("este carro ja foi reservado")
                    else:
                        print("esse carro nao existe")
                else:
                    if opcao == 5:
                        print(f"O total de dinheiro acumulado pelas vendas dos carros é {somavendas}")
                    else:
                        if opcao == 6:
                            indice = 0
                            qnt = 0
                            for n in status:
                                if n == 3:
                                    qnt += 1    
                                indice +=1
                            print("carros livres: {}" .format(qnt))
                            indice = 0
                            qnt = 0
                            for n in status:
                                if n == 2:
                                    qnt += 1
                                indice += 1
                            print("carros reservados: {}".format(qnt))
                            indice = 0
                            qnt = 0
                            for n in status:
                                if n == 1:
                                    qnt += 1
                                indice += 1
                            print("carros vendidos: {}".format(qnt))
                        else:
                            if opcao == 7:
                                iplaca = input("Digite a placa do carro que voce deseja reservar:")
                                carroreservado = False
                                carrovendido = False
                                if verificarplaca(placas,iplaca)== True:
                                    indice = 0
                                    for n in placas:
                                        if n == iplaca and status[indice] == 3:
                                            status[indice] = 2
                                        else:
                                            if n == iplaca and status[indice] == 2:
                                                carroreservado = True
                                            else:
                                                if n == iplaca and status[indice] == 1:
                                                    carrovendido = True
                                        indice+=1
                                    if carroreservado == True:
                                        print("o carro ja foi reservado")
                                    else:
                                        if carrovendido == True:
                                            print(" o carro ja foi vendido")
                                else:
                                    print("o carro nao existe")
                            else:
                                if opcao == 8:
                                    print("A quantidade carros com dados atualizados é {}" .format(qntcarrosatualizados))
                                else:
                                    if opcao == 9:
                                        indice = 0
                                        qnt = 0
                                        for n in precos:
                                            if n > 50000 and status[indice] == 3:
                                                qnt += 1
                                            indice+=1
                                        print("A quantidade de carros livres com preço maior que 50mil é {}" .format(qnt))
                                    elif opcao == 10:
                                        pergunta1 = int(input("Qual é o tempo de uso maximo que voce deseja no carro?:"))
                                        pergunta2 = float(input("Qual o valor maximo que voce deseja pagar no carro?"))
                                        indice = 0
                                        print("Os carros nesse valor sao:")
                                        for n in precos:
                                            if n < pergunta2 and status[indice] == 3:
                                                print(modelos[indice])
                                            indice+=1
































