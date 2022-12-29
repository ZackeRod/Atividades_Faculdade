
#Validando a Entrada

# entrada = int(input('Digite um valor maior do que dez:'))
# while (entrada < 10):
#     entrada = int(input('Digite um valor maior do que dez:'))
# print('Você digitou {}. Encerrando o Programa...'.format(entrada))



# Interompendo um loop com break
#
print('Digite uma mensagem que irei repetir para você!')
print('Para encerrar escreva "sair".')
while True:
    texto = input('')
    print(texto)
    if texto == 'sair':
        break
print('Encerrando o programa...')


#Voltando ao inicio do laço com continue

# while True:
#     nome = input('Qual o seu nome?')
#     if (nome != 'zackerod'):
#         continue
#     senha = input('Qual a sua senha?')
#     if (senha == '123'):
#      break
# print('Acesso concedido.')
