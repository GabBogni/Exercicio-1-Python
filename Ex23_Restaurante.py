"""
Considere o sistema que o cadastro e avaliação que clientes de vão a um determinado restaurante. Nesse sistema, deve permitir:  

- Cadastrar um cliente com seu (nome, e-mail, avaliação e número de estrelas).  Garanta que o e-mail possua um @. Não permita cadastro com duplicidade de e-mail. O campo de avaliação será um texto escrito pelo usuário.

- Listar as avaliações, exibindo-se primeiro as avaliações 5 estrelas, depois 4 estrelas, 3 estrelas e assim por diante.

- Crie uma classificação automática de avaliações em positivas ou negativas. Para fazer essa classificação você deve se basear exclusivamente no texto da avaliação escrito. Procure nesse texto os termos [“bom”, “excelente”, “ótimo”] para dizer se uma avaliação é “positiva” ou os termos [“ruim”, “péssimo”, “horrível”] para classificar ao avaliação como “negativa.” Caso não tenha certeza sobre a avaliação classifique-a como “indeterminada”

- Atualizar uma avaliação: o usuário digita o e-mail cadastrado e, caso ele esteja cadastrado, deve ser possível atualizar o texto da avaliação. Se o e-mail não estiver cadastrado o usuário pode optar por cadastrar o usuário.

- Informar qual a nota média do restaurante (baseado no número de estrelas)

"""

from time import sleep
opcao = 5
listadeclientes = []
listadecomentariospositivos = ["legal","aconchegante","bonito","agradavel","agradável","bom","interessante","excelente","ótimo","otimo"]
listadecomentariosnegativos = ["péssimo","pessimo","horrivel","horrível","desagradavel","desagradável","feio","nojento","sujo","porco","terrivel","terrível","ruim"]
class Cliente:
  def _init_(self):
    self.email = ""
    self.nome = ""
    self.estrelas = 0
    self.comentario = ""

def VerificarEmailValido(email):
  emailvalido = False
  if email.count("@") == 1 and email.count(".com") == 1:
    emailvalido = True
  return emailvalido

def VerificarEmailExiste(email,lista):
  emailexiste = False
  for n in lista:
    if n.email == email:
      emailexiste = True
  return emailexiste

def VerificarClassificação(estrelas):
  classificacaocorreta = False
  if estrelas <= 5 and estrelas >=0:
    classificacaocorreta = True
  return classificacaocorreta

def Avaliarcomentario(comentario):
  soma = 0
  avaliacao = "ERROR"
  comentario2 = comentario.lower()
  palavras = comentario2.split(" ")
  for n in palavras:
    for x in listadecomentariospositivos:
      if n == x:
        soma += 1
    for y in listadecomentariosnegativos:
      if n == y:
        soma -= 1
  if soma > 0:
    avaliacao = "positivo"
  elif soma < 0:
    avaliacao = "negativo"
  else:
    avaliacao = "indefinido"
  return avaliacao    

def CadastrarCliente(lista):
  novocliente = Cliente()
  print("Primeiramente antes de opinar precisamos saber quem é você")
  email = input("Digite o seu email:")
  if VerificarEmailValido(email) == True:
    if VerificarEmailExiste(email,listadeclientes) == False:
      nome = input("Digite seu nome:")
      estrelas = int(input("Digite o numero de estrelas de 0 a 5:"))
      if VerificarClassificação(estrelas) == True:
        comentario = input("Adicione um comentario a sua classificação:")
        novocliente.email = email
        novocliente.nome = nome
        novocliente.estrelas = estrelas
        novocliente.comentario = comentario
        listadeclientes.append(novocliente)
      else:
        print("Sua classificação foi invalida")
    else:
      print("O email já existe")
  else:
    print("O email é invalido")

def Atualizarclassificacao(lista):
  email = input("Digite seu email para sabermos quem é você:")
  if VerificarEmailValido(email) == True:
    if VerificarEmailExiste(email,listadeclientes) == True:
      for n in lista:
        if n.email == email:
          n.comentario = input("Digite o novo comentario:")
    else:
      print("O email não existe!")
  else:
    print("O email é invalido")
  
def Listarclassificacoes(lista):
  listadeestrelas = []
  for n in lista:
    listadeestrelas.append(n.estrelas)
  listadeestrelas.sort()
  listadeestrelas.reverse()
  for x in listadeestrelas:
    for n in lista:
      if x == n.estrelas:
        print("NOME:{}".format(n.nome))
        print("CLASSIFICAÇÃO:{} estrelas".format(n.estrelas))
        print('COMENTARIO:"{}"'.format(n.comentario))
        print("RESUMO DO COMENTARIO:{}".format(Avaliarcomentario(n.comentario)))
        print("_"*20)
        sleep(0.3)
def CalcularMediaDoRestaurante(lista):
  somadeestrelas = 0
  somadecomentarios = 0
  for n in lista:
    somadecomentarios += 1
    somadeestrelas += n.estrelas
  media = somadeestrelas/somadecomentarios
  return media
def Menu():
  print("1 - Opinar sobre o restaurante")
  print("2 - Ver outras opiniões")
  print("3 - Atualizar opinião")
  print("4 - Ver a media de classificação do restaurante")

while opcao != 0:
  Menu()
  opcao = int(input("Digite qual é sua opção:"))
  if opcao == 1:
    CadastrarCliente(listadeclientes)
  elif opcao ==2:
    Listarclassificacoes(listadeclientes)
  elif opcao ==3:
    Atualizarclassificacao(listadeclientes)
  elif opcao ==4:
    print("A media de classifição do restaurante atualmente é {} estrelas".format(CalcularMediaDoRestaurante(listadeclientes)))
  elif opcao == 0:
    print("Tenha um bom dia e volte sempre")



