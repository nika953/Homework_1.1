"""
Напишите программу считающую и обрабатывающую индекс массы тела.
В одной функции программа должна считать ИМТ. В другой обрабатывать, если ИМТ ниже 18.5 печатать "Недостаточный вес",
от 18.5 до 25 "ИМТ в норме", больше 25 "Избыточный вес".
Формула определения ИМТ: index = weight / (height * height)
"""

def get_IMB(weight, height):
    return  weight / (height ** 2)

def check_IMB(index: int) -> None:
    print(index)
    if index < 18.5:
        print('Недостаточный вес')
    elif index < 25:
        print('ИМТ в норме')
    else:
        print('Избыточный вес')

# check_IMB(get_IMB(162, 162))