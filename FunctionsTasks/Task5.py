"""
Каждый стажёр мог выбрать любое число предметов для изучения. По каждому предмету он мог набрать от 0 до 50 баллов.

Программа должна:
Пока пользователь не введет "стоп"":
1. Запрашивать имя студента и число предметов.
2. Запрашивать число баллов по каждому предмету и печатать общую сумму баллов: «Итоговый счёт: _».
3. По сумме баллов опеределять тип грамоты о прохождении стажировки:
- баллов больше 80 — «Наградить дипломом.»;
- баллов больше 50 и меньше или равно 80 — «Наградить похвальной грамотой.»;
- остальные случаи — «Выдать грамоту об участии.».
"""


def count_points():
    result_points = 0
    while (
    flag := input('Для старта напишите что-нибудь. Если вы хотите прекратить программу, напишите "стоп"\n')) != 'стоп':
        name = input('Введите имя: ')
        count_subject = int(input('Введите количество предметов: '))
        for i in range(count_subject):
            points = int(input('Введите количество баллов за один предмет: '))
            result_points += points
        if result_points > 80:
            print('Наградить дипломом')
        elif result_points > 50 and result_points <= 80:
            print('Наградить похвальной грамотой')
        else:
            print('Выдать грамоту об участии')


count_points()