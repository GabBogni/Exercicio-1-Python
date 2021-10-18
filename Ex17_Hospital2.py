"""
Faça um programa para informatizar um hospital. Devem ser salvos os dados dos Pacientes (nome, peso, medico responsável, doença, dias internados) desse hospital.

O programa deve permitir:

- cadastro de pacientes. Não deve ser permitido duplicidade no nome do paciente;

- atualização dos dados do paciente. Deve ser possível atualizar o peso, doença e quantidade de dias internados;

- encontrar o paciente mais magro

- modificação do médico responsável pelo paciente. A partir do nome do paciente, solicitar o nome do novo médico responsável.

- encontrar o paciente mais magro

- encontrar o percentual de pacientes internados com dengue

- criar uma lista com todos os médicos que fazem algum atendimento. Deve ser percorrido o cadastro dos pacientes e verificado todo nome de médico existente. Não deve haver repetição nessa lista.

- encontrar o médico que possui a maior quantidade de pacientes internados;

- considerando que cada médico recebe R$ 100,00 por dia de cada paciente que deixa internado, informe qual o médico que receberá o maior valor.
"""

from time import sleep

listadepacientes = []
opcao = 10


class Paciente:
    def _unit_(self):
        self.nome = ""
        self.peso = 0
        self.medico = ""
        self.doenca = ""
        self.dias = 0
        self.rendamedico = 0


def VerificarNome(paciente):
    pacienteexiste = False
    for n in listadepacientes:
        if n.nome == paciente:
            pacienteexiste = True
    return pacienteexiste


def MostrarMenu():
    print("_" * 20)
    print("Digite a opção desejada:")
    print("1 - Cadastrar paciente")
    print("2 - Atualizar paciente")
    print("3 - Encontrar o paciente mais magro")
    print("4 - Modificar medico do paciente")
    print("5 - Encontrar percentual de pacientes internados por dengue")
    print("6 - Listas os medicos")
    print("7 - Encontrar o medico que possui mais pacientes internados")
    print("8 - O medico que recebe mais de acordo com a quantiadade de pacientes")


def Cadastrarpaciente(lista):
    novopaciente = Paciente()
    nome = input("Digite o nome do paciente:")
    if VerificarNome(nome) == False:
        medico = input("Digite o nome do medico:")
        peso = float(input("Digite o peso do paciente:"))
        doenca = input("Digite a doenca do paciente:")
        dias = float(input("Digite a quantidade de dias do paciente:"))
        novopaciente.nome = nome
        novopaciente.peso = peso
        novopaciente.medico = medico
        novopaciente.doenca = doenca
        novopaciente.dias = dias
        novopaciente.rendamedico = dias*100
        listadepacientes.append(novopaciente)
    else:
        print("O paciente citado já existe")


def AtualizarPaciente(lista):
    nome = input("Digite o nome do paciente de que voce deseja mudar dados:")
    if VerificarNome(nome) == False:
        peso = float(input("Digite o novo peso do paciente:"))
        doenca = input("Digite a nova doenca do paciente:")
        dias = float(input("Digite a nova quantidade de dias do paciente:"))
        for n in lista:
            n.peso = peso
            n.doenca = doenca
            n.dias = dias


def EncontrarMagro(lista):
    menor = 999
    nome = ""
    for n in lista:
        if n.peso < menor:
            menor = n.peso
            nome = n.nome
    return nome


def EncontrarPacientesDengosos(lista):
    total = 0
    dengosos = 0
    porcentagem = 0
    for n in lista:
        total += 1
        if n.doenca == "dengue":
            dengosos += 1
    porcentagem = dengosos / total * 100
    return porcentagem


def VerGanhoCadaMedico(lista):
    qntpacientes = 0
    qntdehoras = 0
    ganho = 0
    medico = ""


def ListarMedicos(lista):
    listademedicos = []
    for n in lista:
        listademedicos.append(n.medico)
    for n in listademedicos:
        if listademedicos.count(n) >=2:
            listademedicos.remove(n)
    return listademedicos

def ModificarMedico(lista):
    nome = input("Digite o nome do paciente do qual voce deseja alterar o medico:")
    for n in listadepacientes:
        if n.nome == nome:
            medico = input("Digite o nome do novo medico:")
            n.medico = medico
            print("Atualização realizada com sucesso")
        else:
            print("O nome do paciente não existe")

def EncontrarMedicoComMaisPaciente(lista):
    copiadalista = []
    listaderepetidos = []
    maior = 0
    medico = ""
    for n in lista:
        copiadalista.append(n.medico)
    for n in lista:
        contador = 0
        for x in copiadalista:
            if n.medico == x:
                contador += 1
        if contador > maior:
            maior = contador
            medico = n.medico
    return medico

def EncontrarMedicoMaisRico(lista):
    copiadalista = []
    listaderepetidos = []
    medico = ""
    maior = 0
    for n in lista:
        copiadalista.append(n.medico)
    for n in lista:
        salario = 0
        for x in copiadalista:
            if n.medico == x:
                salario += n.rendamedico
        if salario > maior:
            maior = salario
            medico = n.medico
    maior = maior/2
    print("{} é o medico que tem um salário maior, sendo {}".format(medico, maior))


while opcao != 0:
    MostrarMenu()
    opcao = int(input("Digite a opcao desejada:"))
    if opcao == 1:
        Cadastrarpaciente(listadepacientes)
    elif opcao == 2:
        AtualizarPaciente(listadepacientes)
    elif opcao == 3:
        print("O paciente mais magro é {}".format(EncontrarMagro(listadepacientes)))
    elif opcao == 4:
        ModificarMedico(listadepacientes)
    elif opcao == 5:
        print("A porcentagem de pacientes dengosos é {}".format(EncontrarPacientesDengosos(listadepacientes)))
    elif opcao ==6:
        print(ListarMedicos(listadepacientes))
    elif opcao ==7:
       print(EncontrarMedicoComMaisPaciente(listadepacientes))
    elif opcao ==8:
        EncontrarMedicoMaisRico(listadepacientes)




