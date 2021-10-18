"""
Considere o cenário de um Hospital. Faça um programa para cadastrar e gerenciar os pacientes. Para cada paciente deve ser cadastrado: nome, idade, sexo e tipo atendimento (1 - plano de saúde, 2 - SUS, ou 3 - Particular). Construa um menu onde é possível:

· Incluir novos pacientes. (incluir um paciente por vez). O sistema não deve permitir que seja cadastrado dois pacientes com o mesmo nome. Se isso ocorrer, o sistema deve informar ao usuário que não é possível cadastrar o hóspede.  Faça uma função para verificar se já existe o paciente.

· Listar todos os dados dos pacientes cadastrados.

· Excluir um paciente a partir do nome. (o usuário deve digitar o nome e o sistema exclui o paciente do sistema). Caso o usuário digite o nome de um paciente que não exista o sistema deve informar que o paciente não existe.

· Exibir os pacientes de determinado tipo de atendimento: O sistema pergunta qual o tipo de atendimento. O usuário deve informar o tipo de atendimento para o qual está buscando a quantidade. O sistema deve exibir na tela os nomes dos pacientes que são do tipo de atendimento que o usuário escolheu. Se o usuário escolher um tipo de atendimento que não exista o sistema deve informar ao usuário que não existe o tipo de atendimento informado.

· Exibir a quantidade de pacientes que tiveram seus dados excluídos.

· Informar a média de idade dos pacientes do sexo feminino

· Possibilitar migração de plano de saúde: o sistema deve perguntar o nome do paciente. Depois de informado o nome, o sistema deve informar qual o plano de saúde e perguntar se o paciente deseja ou não uma migração de plano. Se ele optar por migrar, ele deve escolher um novo plano. Caso o nome do paciente não esteja cadastrado, informar isso para o usuário
"""

escolha = 7
nome = []
sexo = []
idade = []
plano = []
qntclienteex = 0 # Quantidade de clintes excluidos
qntclientesexofem = 0 # Quantidade de clientes do sexo feminino
qnttotaldeclintes = 0 # Quantidade total de clientes
pacienteExiste = 0 # Usada na condição para ver se nome de algum cliente existe. 0 para não e >0 para sim

while escolha != 0:
    print("_"*50)
    print("Digite 0 - para sair")
    print("Digite 1 - para cadastrar um cliente")
    print("Digite 2 - listar todos os clientes")
    print("Digite 3 - excluir um cliente")
    print("Digite 4 - listar os clientes de um plano especifico")
    print("Digite 5 - exibir a quantidade de clientes excluidos")
    print("Digite 6 - informar a media dos clintes do sexo feminino")
    print("Digite 7 - para atualizar um plano de um cliente")
    escolha = int(input("Digite opção desejada"))
    if escolha == 1:
        dignome = input("Digite o nome do cliente que deseja cadastrar")
        for n in nome:
            if n == dignome:
                print("Já existe um cadastro com esse nome")
                pacienteExiste += 1
        if pacienteExiste == 0:
            nome.append(dignome)
            digsexo = input("Digite o sexo do clinte: M para masculino, F para feminino")
            digidade = int(input("Digite a idade do paciente"))
            digplano = int(input("Digite o plano de saude do cliente: \n 1 - Plano de saude \n  2 - SUS \n 3 - Particular"))
            sexo.append(digsexo)
            idade.append(digidade)
            plano.append(digplano)
        pacienteExiste = 0
    if escolha == 2:
        for n in nome:
            print(n)
    else:
        if escolha == 3:
            excluirnome = input("Digite o nome do cliente, do qual deseja excluir o cadastro")
            indice = 0
            for n in nome:
                if n == excluirnome:
                    nome.remove(n)
                    del sexo[indice]
                    del plano[indice]
                    del idade[indice]
                    qntclienteex += 1
                    pacienteExiste +=1
                    print("Dados do paciente excluidos com sucesso")
            indice += 1
            if pacienteExiste == 0:
                print("Esse paciente nao existe")
            pacienteExiste = 0
        else:
            if escolha == 4:
                pergunta = int(input("Digite o plano que possui o cliente que voce deseja ver: \n 1 - Plano de saude \n  2 - SUS \n 3 - Particular"))
                if pergunta == 1:
                    indice = 0
                    print("Plano de saúde:")
                    for n in plano:
                        if n == 1:
                            print(nome[indice])
                        indice+= 1
                else:
                    if pergunta == 2:
                        indice = 0
                        print("SUS:")
                        for n in plano:
                            if n == 2:
                                print(nome[indice])
                            indice+=1
                    else:
                        if pergunta == 3:
                            indice = 0
                            print("Particular:")
                            for n in plano:
                                if n == 3:
                                    print(nome[indice])
                                indice += 1
                        else:
                            print("Não há esse plano que você escolheu")
            else:
                if escolha == 5:
                    print(f"A quantidade de clientes excluidos do sistema é {qntclienteex}")
                else:
                    if escolha == 6:
                        for n in sexo:
                            qnttotaldeclintes += 1
                            if n == "F":
                                qntclientesexofem +=1
                        if qnttotaldeclintes == 0:
                            media = 0
                        else:
                            media = qntclientesexofem / qnttotaldeclintes
                        print("A media da quantidade de clientes do sexo feminino é {}".format(media))
                        qntclientesexofem = 0
                        qnttotaldeclintes = 0
                    else:
                        if escolha == 7:
                            opcao = input("Digite o nome do cliente que voce deseja atualizar os dados")
                            indice = 0
                            for n in nome:
                                if n == opcao:
                                    pacienteExiste += 1
                                    dignovoplano = int(input("Digite o novo plano de saude do cliente: \n 1 - Plano de saude \n  2 - SUS \n 3 - Particular"))
                                    if dignovoplano >= 1 and dignovoplano <= 3:
                                        plano[indice] = dignovoplano
                                    else:
                                        print("Esse plano não existe")
                                indice+= 1
                            if pacienteExiste == 0:
                                print("O paciente citado nao existe")
                            pacienteExiste = 0
