"""
Fazer um programa que manipule listas por meio de funções. Para cada item, faça uma função.  As entradas de dados devem ser feitas no programa principal. As funções devem processar as solicitações e retornar listas e valores. Faça um menu para o usuário poder interagir entre as opções

- fazer uma função para gerar uma lista de números inteiros com a quantidade de elementos que o usuário desejar

- fazer uma função que encontra o maior elemento e o retorna

- fazer uma função que multiplica todos os valores da lista por um número digitado pelo usuário

- fazer uma função que concatena as duas listas

- fazer uma função que gere, a partir de uma lista, a lista com os valores ordenados

- fazer uma função que retira os elementos repetidos de uma lista.

- fazer uma função que mostre todos os números pares da lista.

- fazer uma função que, a partir de duas listas, gere uma com a intersecção dos elementos
"""

escolha = 7
from random import randint
def criarlista(quantidadedetermos):
  x = []
  while quantidadedetermos > 0:
    y = randint(0,10)
    x.append(y)
    quantidadedetermos -= 1
  return x
def encontrarmaiorvalor(lista):
  x = max(lista)
  return x
def multiplicar(valor,nomedalista):
  x = []
  for n in nomedalista:
    n = n * valor
    x.append(n)
  return x
def concatenar(lista1,lista2):
  lista3 = lista1 + lista2
  return lista3
def ordenarlista(lista):
  lista.sort()
  return lista
def retirarrelementosrep(lista):
  for n in lista:
    if lista.count(n) >= 2:
      lista.remove(n)
  return lista
def encontrarelementospares(lista):
  elementospares = []
  for n in lista:
    if n%2 == 0:
      elementospares.append(n)
  return elementospares
def fazerinterseccaodelistas(lista1,lista2):
  lista3 = []
  for n in lista1:
    for n2 in lista2:
      if n == n2:
        lista3.append(n)
  for n in lista3:
    if lista3.count(n) >= 2:
      lista3.remove(n)
  return lista3
def menu():
  print("0 - Sair")
  print("1 - Criar um lista")
  print("2 - Encontrar maior valor da lista")
  print("3 - Multiplicar cada elemento da lista por um valor")
  print("4 - Concatenar uma lista")
  print("5 - Ordenar uma lista em ordem crescente")
  print("6 - Retirar elementos repetitivos de uma lista")
  print("7 - Mostra numeros pares de uma lista")
  print("8 - Mostra interseccao de duas listas")

ordem = 1
listadelista = []
while escolha != 0:
   menu()
   escolha = int(input("Digite a opção desejada"))
   if escolha == 1:
     termos = int(input("Digite a quantidade de termos de uma lista randomica:"))
     print( "lista numero {}".format(ordem))
     ordem += 1
     a = criarlista(termos)
     listadelista.append(a)
     print(a)
   else:
    if escolha == 2:
        numero = int(input("digite o numero que representa a lista que voce deseja ver o maior elemento"))
        print("o maior valor da lista citada é {}".format(encontrarmaiorvalor(listadelista[numero-1])))
    else:
      if escolha == 3:
        numero = int(input("Digite o numero que representa a lista que voce deseja fazer a multiplicação"))
        mult = float(input("Digite um valor pra multiplicar com todos elementos dessa lista"))
        print(multiplicar(mult, listadelista[numero-1]))
      else:
          if escolha == 4:
            numero = int(input("Digite o numero que representa a primeira lista com que voce deseja concatenar"))
            numero2 = int(input("Digite o numero que representa a segunda lista com que voce deseja concatenar"))
            print(concatenar(listadelista[numero-1],listadelista[numero2-1]))
          else:
            if escolha == 5:
              numero = int(input("Digite o numero que representa a lista que voce deseja ordenar"))
              print(ordenarlista(listadelista[numero-1]))
            else:
              if escolha == 6:
                numero = int(input("Digite o numero que representa a lista que voce deseja retirar elementos repetitivos"))
                print(retirarrelementosrep(listadelista[numero-1]))
              else:
                if escolha == 7:
                  numero = int(input("Digite o numero que representa a lista que voce deseja ver elementos pares"))
                  print(encontrarelementospares(listadelista[numero-1]))
                else:
                  if escolha == 8:
                    numero = int( input("Digite o numero que representa a primeira lista com que voce deseja fazer a interseccao"))
                    numero2 = int(input("Digite o numero que representa a segunda lista com que voce deseja fazer a interseccao"))
                    print(fazerinterseccaodelistas(listadelista[numero-1],listadelista[numero2 - 1]))





