#2 while

# tabuada = 1
# while tabuada <= 10:
#     print('TABUADA O {}:'.format(tabuada))
#     i = 1
#     while i <= 10:
#         print('{} x {} = {}'.format(tabuada, i, tabuada * i))
#         i += 1
#     tabuada += 1


#2 for

for tabuada in range(1, 11 , 1):
    print('TABUADA DO {}:'.format(tabuada))
    for i in range(1, 11, 1):
        print('{} x {} = {}'.format(tabuada, i, tabuada * i))


# while + for

# tabuada = 1
# while tabuada <= 10:
#     print('TABUADA DO {}:'.format(tabuada))
#     for i in range(1, 101, 1):
#         print('{} x {} = {}'.format(tabuada, i, tabuada * i))
#     tabuada += 1