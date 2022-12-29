inicial = int(input('Qual valor deseja inicia a contagem?'))
final = int(input('Qual valor deseja encerrar a contagem?'))
x = inicial
while (x <= final):
    if(x % 2 == 0): # SOMENTE NUMEROS PARES
        print(x)
    x = x + 1