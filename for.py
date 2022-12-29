#Estrutura de repetição FOR (para)

# for i in range(6):
#     print(i)

# for i in range(1,6,1):
#     print(i)

# for i in range(10,0,-2):
#     print(i)

# Exercicios

soma = 0
qtd = 0
for i in range(1,101):
    if (i % 2 == 0):
        soma += i
        qtd += 1
media = soma / qtd
print('A média dos pares de 1 até 100 é: {}.'.format(media))