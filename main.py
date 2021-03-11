from random import randrange
from Utils import Sistema

# Quadro de chegada - (TEMPO em unidade de tempo, PROBABILIDADE) 
# EXEMPLO: quadroDeChegada = [
#    (0,0.2),
#    (2,0.4),
#    (5,0.4),
#    ]
quadroDeChegada = [
    (0,0.2),
    (1,0.3),
    (3, 0.4),
    (6, 0.1)
    ]

# Quadro de Tempo de atendimento - (TEMPO em unidade de tempo, PROBABILIDADE) 
# EXEMPLO: quadroDeAtendimento = [
#    (1.5,0.2),
#    (4,0.4),
#    (6,0.4),
#    ]
quadroDeAtendimento = [
    (1,0.3),
    (2,0.4),
    (3,0.3)
]

# Número de usuários para ser realizada simulação
numeroDeUsuarios = 20



sistema = Sistema(quadroDeChegada,quadroDeAtendimento,numeroDeUsuarios)
sistema.calcular()
sistema.mostrarTabela()
