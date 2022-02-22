# from random import choice
# import random
# import random as rd

"""from random import (
    random,
    choice
)

print(random())

lista = ["Pedro", "Tiago", "João"]
print(choice(lista))"""

"""from random import randint

print(randint(1, 5))"""

"""
Módulos - arquivos com extensão .py (arquivos python)
Pacotes - diretórios contendo um conjunto de módulos
"""

from pacote import principal, secundario
from pacote.subpacote import outros


__doc__ = "Esse módulo tem como objetivo efetuar somas, quadráticas e cúbicas"

print(principal.soma(5, 7))
print(secundario.quadratica(10))
print(outros.cubica(3))
