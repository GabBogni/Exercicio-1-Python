"""
Considere o sistema que faz cadastro de palavras em um dicionário. São armazenados, além da própria palavra, os sinônimos, separados por “;” e sua classe gramatical. Faça um sistema onde é possível:

 

Cadastrar um termo, evitando a duplicidade

Listar os termos, com seus vários sinônimos em tópicos numerados

Calcular para cada termo o tamanho de caracteres necessários para armazenar e a quantidade de sinônimos de cada termo. Exibir essas informações na listagem de termos.

Adicionar um novo sinônimo a um termo: O usuário digita o termo. O sistema lista seus sinônimos e para o usuário informar qual o novo sinônimo que será inserido.  O usuário digita o novo sinônimo e confirma a operação.

Informar qual o termos que possui a maior quantidade de sinônimos.

Listar todos os termos de uma determinada classe gramatical digitada pelo usuário.

Excluir um termo

Excluir um sinônimo de um determinado termo.

 

Exemplo de um termo:

 

Termo: problema

Sinônimos: contrariedade;  adversidade; contratempo;  dificuldade

Classe: Substantivo 
"""

from time import sleep
escolha = 8
listadetermos = []
class Termo:
    def _init_(self):
        self.sinonimos = []
        self.nome = ""
        self.classe = ""
def Menu():
    print("1 - Cadastrar um termo no dicionario")
    print("2 - Listar os termos do dicionario e seus sinonimos")
    print("3 - Adicionar um sinonimo a um termo")
    print("4 - Informar qual termo possui a maior quantidade de sinonimos")
    print("5 - Listar todos termos de uma classe gramatical especifica")
    print("6 - Excluir um termo")
    print("7- Excluir um sinonimo de um termo")
    print("0 - Sair")
def VerificarNome(nome,lista):
    nomeexiste = False
    for n in lista:
        if n.nome == nome:
            nomeexiste = True
    return nomeexiste
def VerificarSinonimo(nomedotermo,nomedosinonimo,lista):
    nomeexiste = False
    for n in lista:
        for x in n.sinonimos:
            if x == nomedosinonimo and n.nome == nomedotermo:
                nomeexiste = True
    return nomeexiste
def Informarqualpossuimaissinonimos(lista):
  maior = 0
  for n in lista:
    if len(n.sinonimos) > maior:
      maior = len(n.sinonimos)
      nomedomaior = n.nome
  return nomedomaior
def CadastrarTermo(lista):
    novotermo = Termo()
    nome = input("Digite o nome do termo a ser inserido no sistema:")
    nome.lower()
    if VerificarNome(nome,listadetermos) == False:
        novotermo.classe = input("Digite o nome da classe gramatical do termo").lower()
        novotermo.nome = nome
        novotermo.sinonimos = []
        lista.append(novotermo)
        print("Termo registrado com sucesso")
    else:
        print("O nome digitado já existe")
def CadastrarSinonimos(lista):
    nome = input("Digite o nome do termo no qual você deseja adicionar um sinonimo:")
    if VerificarNome(nome,listadetermos) == True:
        sinonimo = input("Digite o nome do sinonimo que deseja acrescentar no termo:")
        if VerificarSinonimo(nome,sinonimo,listadetermos) == False:
            for n in lista:
                if n.nome == nome:
                    sinonimo.lower()
                    n.sinonimos.append(sinonimo)
                    print("Sinonimo registrado com sucesso")
        else:
            print("Já existe esse sinonimo registrado nesse termo")
    else:
        print("O termo digitado não existe")

def ListarTermos(lista):
    for n in lista:
        print("NOME:{}".format(n.nome))
        if len(n.sinonimos) == 0:
            print("SINONIMOS: Nenhum")
        else:
            print("SINONIMOS: {}".format(n.sinonimos))
        print("CLASSE GRAMATICAL:{}" .format(n.classe))
        print("NÚMERO DE CARACTERES: {}".format(len(n.nome)))
        print("NÚMERO DE SINONIMOS: {}".format(len(n.sinonimos)))
        print("_" * 20)
        sleep(0.3)
def ExcluirTermos(lista):
    nome = input("Digite o nome do termo:")
    if VerificarNome(nome,listadetermos) == True:
        for n in lista:
            if nome == n.nome:
                lista.remove(n)
                print("Termo removido com sucesso")
    else:
        print("O termo digitado não existe")
def ExcluirSinonimos(lista):
    nomedotermo = input("Digite o nome do termo no qual tem o sinonimo a ser deletado:")
    if VerificarNome(nomedotermo,listadetermos) == True:
        nomedosinonimo = input("Digite o nome do sinonimo a ser deletado").lower()
        if VerificarSinonimo(nomedotermo,nomedosinonimo,listadetermos) == True:
            for n in lista:
                for x in n.sinonimos:
                    if x == nomedosinonimo:
                        n.sinonimos.remove(x)
                        print("Sinonimo deletado com sucesso")
        else:
            print("Esse sinonimo não existe no termo digitado")
    else:
        print("Esse termo não existe")
def Listarporclasse(lista):
    listadeclasses = []
    for n in lista:
        listadeclasses.append(n.classe)
    for n in listadeclasses:
        print("LISTA DE {}:".format(n))
        for x in lista:
            if n == x.classe:
                print(x.nome)
        print("_"*20)
        sleep(0.3)


while escolha != 0:
    Menu()
    escolha = int(input("Digite a opção desejada:"))
    if escolha ==1:
        CadastrarTermo(listadetermos)
    elif escolha==2:
        ListarTermos(listadetermos)
    elif escolha==3:
        CadastrarSinonimos(listadetermos)
    elif escolha==4:
        print("O termo que possui mais sinonimos é {}".format(Informarqualpossuimaissinonimos(listadetermos)))
    elif escolha==5:
        Listarporclasse(listadetermos)
    elif escolha==6:
        ExcluirTermos(listadetermos)
    elif escolha==7:
        ExcluirSinonimos(listadetermos)


