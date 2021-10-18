"""
Faça uma calculadora que com menu com as operações de soma, subtração, multiplicação e divisão.
"""

opcao = -1
while opcao != 0:
    print("____Menu______")
    print("0 -Sair")
    print("1 -Somar")
    print("2 -Subtrair")
    print("3 -Multiplicacao")
    print("4 -Divisao")
    opcao = float(input("Digite a opcao"))
    if opcao == 1:
        n1 = float(input("Digite o primeiro numero"))
        n2 = float(input("Digite o segundo numero"))
        print("O resultado da soma é {}".format(n1 + n2))
    else:
        if opcao == 2:
            n1 = float(input("Digite o primeiro numero"))
            n2 = float(input("Digite o segundo numero"))
            print("O resultado da subtracao é {}".format(n1 - n2))
        else:
            if opcao == 3:
                n1 = float(input("Digite o primeiro numero"))
                n2 = float(input("Digite o segundo numero"))
                print("O resultado da multiplicacao é {}".format(n1 * n2))
            else:
                if opcao == 4:
                    n1 = float(input("Digite o primeiro numero"))
                    n2 = float(input("Digite o segundo numero"))
                    if n2 != 0:
                        print("O resultado divisao é {:.2f}".format(n1 / n2))
                    else:
                        print("A divisao por 0 nao existe")
                else:
                    if opcao == 0:
                        print("Tenha um bom dia")
