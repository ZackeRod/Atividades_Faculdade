#Estrutura de repetição FOR (para)

# for i in range(6):
#     print(i)

# for i in range(1,6,1):
#     print(i)

# for i in range(10,0,-2):
#     print(i)

# Exercicios

soma = 0
qtd = 1
for cont in range(0, 6, 1):
    print('Valor de i: {}.'.format(cont))
    if (cont % 2 == 0):
        soma += cont
        qtd += 1
media = soma / qtd
print('A média dos pares de 1 até 100 é: {}.'.format(media))