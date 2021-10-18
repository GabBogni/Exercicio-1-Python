"""
Considere o sistema de uma fábrica que faz o cadastro de funcionários. São armazenados sobre cada funcionário o seu nome, valor da hora de trabalho,  a quantidade de horas trabalhadas e departamento. Faça um sistema onde é possível:

Cadastrar um departamento (somente nome)

Listar os departamentos

Cadastrar um funcionário. Para cadastro de funcionário o valor da hora de trabalho deve ser maior que R$ 5,00 e o departamento deve estar na lista dos departamentos cadastrados.

Listar os funcionários

Calcular o salário de cada funcionário considerando que ele recebe o valor de horas trabalhadas multiplicado pelo valor hora até 200 horas no mês. Se ele ultrapassar esse valor de horas trabalhadas, as horas que excederem 200 devem ser multiplicadas pelo dobro.

Exibir o nome do funcionário que que vai receber o maior salário no mês

Informar o departamento que tem a maior folha de pagamento.

Excluir os funcionários nos quais a quantidade de horas no mês seja menor que algum valor informado pelo usuário
"""

from time import sleep
escolha = 10
listadefuncionarios = []
listadedepartamentos = []
class Funcionarios:
  def __init__(self):
    self.nome = ""
    self.valordahora = 0
    self.departamento = ""
    self.horasmensais = 0
  
def Menu():
  print("_"*30)
  print("1 - Cadastrar um departamento")
  print("2 - listar os departamentos")
  print("3 - Cadastrar um funcionario")
  print("4 - listar os funcionarios")
  print("5 - Calcular o salario de um funcionario")
  print("6 - Exibir o nome do funcionario que recebera o maior salario do mes")
  print("7 - Informar departamento que possui a maior folha de pagamento")
  print("8 - Excluir funcinarios do sistema que possuam uma jornada de trabalho menor que um valor determinado")
def VerificarNome(nome,lista):
  nomeexiste = False
  for n in lista:
    if n.nome == nome:
      nomeexiste = True
  return nomeexiste
def VerificarDepartamento(nome,lista):
  nomeexiste = False
  for n in lista:
    if n == nome:
      nomeexiste = True
  return nomeexiste
def VerificarValorHora(valor):
  valoraceitavel = False
  if valor > 5:
    valoraceitavel = True
  return valoraceitavel
  
def CadastrarFuncionarios(lista):
  objfuncionario = Funcionarios()
  nome = input("Digite o nome do funcionario:")
  if VerificarNome(nome,listadefuncionarios) == False:
    departamento = input("Digite o nome do departamento, o qual  o funcionario pertence")
    if VerificarDepartamento(departamento,listadedepartamentos) == True:
      valordahora = float(input("Digite o custo por hora do funcionario:"))
      if VerificarValorHora(valordahora) == True:
        objfuncionario.nome = nome
        objfuncionario.departamento = departamento
        objfuncionario.valordahora = valordahora
        lista.append(objfuncionario)
        objfuncionario.horasmensais = float(input("Digite a quantidade de horas mensais do funcionario"))
        print("Registro realizado com sucesso")
      else:
        print("O valor precisa ser superior a 5 reais por hora")
    else:
      print("Esse departamento não existe")
  else:
    print("Esse nome já existe")
      

def CadastrarDepartamento(lista):
  nome = (input("Digite o nome do departamento"))
  if VerificarDepartamento(nome,listadedepartamentos) == False:
    lista.append(nome)

def ListarDepartamentos(lista):
  for n in lista:
    print(n)

def ListarFuncionarios(lista):
  for n in lista:
    print("_"*30)
    print("NOME:"+n.nome)
    print("DEPARTAMENTO:"+n.departamento)
    print("VALOR POR HORA:{}".format(n.valordahora))
    print("HORAS MENSAIS TRABALHADAS:{}".format(n.horasmensais))
    sleep(1)
def CalcularSalario(lista):
  nome = input("Digite o nome do funcionario:")
  salario = 0
  if VerificarNome(nome,listadefuncionarios) == True:
    for n in lista:
      if n.nome == nome:
        if n.horasmensais > 200:
          salario = (n.valordahora * 200) + ((n.horasmensais - 200) * 2 * n.valordahora)
        else:
          salario = n.valordahora * n.horasmensais
  else:
    print("Esse nome não existe")
  return salario
def VerFuncionarioMaisRico(lista):
  maior = 0 
  funcionario = ""
  for n in lista:
    if n.horasmensais > 200:
          salario = (n.valordahora * 200) + ((n.horasmensais - 200) * 2 * n.valordahora)
    else:
          salario = n.valordahora * n.horasmensais
    if salario > maior:
      maior = salario
      funcionario = n.nome
  return funcionario

def VerDepartamentoMaisRico(lista):
  dinheiro = 0
  departamento = ""
  copiadalista = []
  maior = 0
  for n in lista:
    copiadalista.append(n)
  for n in lista:
    dinheiro = 0
    for x in copiadalista:
      if x.horasmensais > 200:
          salario = (x.valordahora * 200) + ((x.horasmensais - 200) * 2 * x.valordahora)
      else:
          salario = x.valordahora * x.horasmensais
      if n.departamento == x.departamento:
        dinheiro += salario
    if dinheiro > maior:
      maior = dinheiro
      departamento = n.departamento
  print("O departamento {} possui a maior folha de pagamento com {} por mes".format(departamento,maior))
def ExcluirFuncionario(lista):
  tempo = int(input("Digite a quantidade de horas minimas que um funcionario precisa trabalhar por mês"))
  for n in lista:
    if n.horasmensais < tempo:
      lista.remove(n)
      print("Funcionarios removidos com exito")

while escolha != 0:
  Menu()
  escolha = int(input("Escolha uma opcao:"))
  if escolha ==1:
    CadastrarDepartamento(listadedepartamentos)
  elif escolha == 2:
    ListarDepartamentos(listadedepartamentos)
  elif escolha == 3:
    CadastrarFuncionarios(listadefuncionarios)
  elif escolha ==4:
    ListarFuncionarios(listadefuncionarios)
  elif escolha ==5:
    print("O salario desse funcionario é R${}" .format(CalcularSalario(listadefuncionarios)))
  elif escolha ==6:
    print("O funcionario que recebe mais é "+VerFuncionarioMaisRico(listadefuncionarios))
  elif escolha ==7:
    VerDepartamentoMaisRico(listadefuncionarios)
  elif escolha ==8:
    ExcluirFuncionario(listadefuncionarios)