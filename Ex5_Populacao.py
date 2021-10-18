"""
Dado um pais A, com 5000000 de habitantes e uma taxa de natalidade de 3% ao ano, e um pais B com 7000000 de habitantes e uma taxa de natalidade de 2% ao ano, escrever um algoritmo que seja capaz de calcular e iterativamente e no fim imprimir o tempo necessário para que a população do pais A ultrapasse a população do pais B.
"""

loop = 1
popAatual = 5000000
popBatual = 7000000
nanos = 0
while loop == 1:
    popAatual = popAatual + popAatual/ 100 * 3
    popBatual = popBatual + popBatual/100 *2
    nanos += 1
    if popAatual > popBatual:
        loop = 0
print("Resposta -> O numero de anos necessario para a população de A superar a de B é {}" .format(nanos))