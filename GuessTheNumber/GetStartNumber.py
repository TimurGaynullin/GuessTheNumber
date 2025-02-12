'''
Функция не принимает никакие параметры.
Функция должна:
1. Попросить пользователя ввести конечное число.
2. Если пользователь ввел не число или отрицательное число, то вывести ошибку и попросить пользователя ввести число еще раз.
3. Если число подходит, то вернуть его.
'''
from GuessTheNumber.IsPositiveNumber import IsPositiveNumber


# Это задание выполнит Никита


def GetStartNumber():
    print('Введите стартовое число:')
    StartNumber = input()
    if IsPositiveNumber(StartNumber):
        return int(StartNumber)
    else:
        print('Введено неверное значение. Возможно вы ввели текст или отрицательное число, введите положительное число и повторите попытку')
        return GetStartNumber()

GetStartNumber()