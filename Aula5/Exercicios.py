# Escreva uma rotina que crie uma borda ao redor de uma palavra
# para destacá-la como sendo um título. A rotina deve receber como
# parâmetro a palavra a ser destacada. O tamanho da caixa de texto
# deverá ser adaptável de acordo com o tamanha da palavra.

# Exercício 1

# def borda(s1):
#     tam = len(s1)
#     # Só imprime caso exista alguma caractere
#     if tam:
#         print('+','-' * tam,'+')
#         print('|',s1,'|')
#         print('+','-' * tam,'+')
#
# # Programa Principal
# borda('Olá, Mundo!')
# borda('Lógica de Programação e Algaritmos')



# Exercício 2
def valida_string(pergunta, min, max):
    s1 = input(pergunta)
    tam = len(s1)
    while ((tam < min) or (tam > max)):
        print('Palavra Inválida!')
        s1 = input(pergunta)
        tam = len(s1)

    return s1

# Programa principal
x = valida_string('Digite um string: ', 10, 30)
print('Você digitou a string: {}. \n Dado válido. Encerrando o programa...'.format(x))