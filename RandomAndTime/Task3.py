"""
На летней универсиаде будет проводиться по два забега. Чтобы соревнования были честными,
участники должны распределяться между забегами случайным образом.
Напишите программу, печатающую случайные номера забегов (1 или 2) до тех пор, пока не будет введено «off».
После генерации каждого номера должно печататься:
1) «Ваш номер: _».
2) «Участников в первом забеге: _», «Участников во втором забеге: _».
"""

from random import *

def competition(first_comp, second_comp):
    while a := input('Для остановки программы введите off\nИмя участника: ') != 'off':
        number = randint(1, 2)
        print('Ваш номер: ', number)
        if number == 1:
            first_comp += 1
        else:
            second_comp += 1
        print(f'Участников в первом забеге: {first_comp}, Участников во втором забеге: {second_comp}')

competition(0, 0)