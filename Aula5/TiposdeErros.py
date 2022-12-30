# while True:
#     try:
#         x = int(input('Por favor digite um número: '))
#         print('Você Digitou o Número: {}, Encerrando Programa...'.format(x))
#         break
#     except ValueError:
#         print('Oops! Dígito inválido. Tente novamente...')



# def div():
#     try:
#         num1 = int(input('Digite um número: '))
#         num2 = int(input('Digite mais um número: '))
#         res = num1 / num2
#     except ZeroDivisionError:
#         print('Oops: Erro de divisão por zero...')
#     except:
#         print('Algo de errado aconteceu...')
#     else:
#         return res
#     finally:
#         print('Executará sempre!')
#
# # Programa principal
# print(div())



# def imprime_com_condicao(num, fcond):
#     if fcond(num):
#         print(num)
#
# def par(x):
#     return x % 2 == 0
# def impar(x):
#     return not par(x)
#
# # Programa principal
# imprime_com_condicao(5, impar)

# funções lambda

res = lambda x: x * x
print(res(3))

soma = lambda x, y: x + y
print(soma(3,5))