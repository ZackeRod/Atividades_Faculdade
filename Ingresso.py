# Exercício 3
#
# Um cinema cobra preços diferentes para os ingressos
# de acordo com a idade de uma pessoa. Se a pessoa tiver
# menos de 3 anos de idade, o ingesso será gratuito, se tiver
# entre 3 e 12 anos, o ingesso custará R$ 15, se tiver
# mais de 12 anos, custará R$ 30.

#1ª- Escreva um laço em que você pergunte a idade aos
#    usuários e, então, informe-lhes o preço do ingresso
#    do cinema.

#2ª- Encerre o laço usando um break quando o usuário digitar sair.

#3ª- Após encerrar o laço, apresenta na tela o total de pessoas
#    que compraram ingressos, o total de dinheiro arrecadado
#    e a média de idade das pessoas.

total = 0
dinheiro = 0

while True:
    idade = input('Qual sua idade?')
    if idade == 'sair':
        break
    idade = int(idade)
    total += 1
    if idade < 3:
        ingresso = 0
    else:
        if idade > 12:
            ingresso = 30
        else:
            ingresso = 15
    dinheiro += ingresso

media = dinheiro / total
print('Total de Pessoas {}'.format(total))
print('Dinheiro Total Arrecadado {}'.format(dinheiro))
print('Média Total Arrecadada {}'.format(media))
print('Programa Finalizado Com Sucesso!')