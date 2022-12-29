# Escreva um algoritmo que leia dois valores numéricos e
# que pergunte ao usuário qual operação ele deseja realizar:
# adição(+), subtração(-), multiplicação(*), divisão(/) e sair.
# exiba na tela o resultado da operação desejada.

# 1ª- REPITA ATÉ QUE A OPÇÃO SAÍDA SEJA ESCOLHIDA
# 2ª- (EXERCÍCIO CONSTRUIDO NA AULA PRÁTICA 3)

print('CALCULADORA')
print('+ Adição')
print('- Subtração')
print('* Multiplicação')
print('/ Divisão')
print('Presione outra tecla para sair')

# op = input('Qual operação deseja fazer?')
# if op == '+' or op == '-' or op == '*' or op == '/':
#     x = int(input('Digite o primeiro valor:'))
#     y = int(input('Digite o segundo valor:'))

while True:
    op = input('Qual operação deseja fazer?')  #NOVO MODELO
    if op == '+' or op == '-' or op == '*' or op == '/':
        x = int(input('Digite o primeiro valor:'))
        y = int(input('Digite o segundo valor:'))

# while (op != 's'):
    if (op == '+'):
        res = x + y
        print('Resultado {} + {} = {}'.format(x, y, res))
    elif (op == '-'):
        res = x - y
        print('Resultado {} - {} = {}'.format(x, y, res))
    elif (op == '*'):
        res = x * y
        print('Resultado {} * {} = {}'.format(x, y, res))
    elif (op == '/'):
        res = x / y
        print('Resultado {} / {} = {}'.format(x, y, res))
    elif (op == 's'):  # Outro Modelo
        break # Outro modelo
    else:
        print('Operação inválida!')

    # op = input('Qual operação deseja fazer?')
    # if op == '+' or op == '-' or op == '*' or op == '/':
    #     x = int(input('Digite o primeiro valor:'))
    #     y = int(input('Digite o segundo valor:'))

print('Encerrando o programa...')