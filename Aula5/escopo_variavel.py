# def comida():
#     print(ovos)
#
# # Programa Principal
# ovos = 12
# comida()

# def comida():
#     ovos = 12
#     bacon()
#     print(ovos)
#
# def bacon():
#     ovos = 6
#
# # Programa Principal
# comida()




# def comida():
#     ovos = 'Variável local de comida'
#     print(ovos)
#
# def bacon():
#     ovos = 'Variável local de bacon'
#     print(ovos)
#     comida()
#     print(ovos)
#
# # Programa Principal
# ovos = 'Variável Global'
# bacon()
# print(ovos)




# A Instrução global
def comida():

    ovos = 'comida'

#Programa Principal
ovos = 'Global'
comida()
print(ovos)