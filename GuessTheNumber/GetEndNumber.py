'''
Эта функция должна принять одно число (начальное число, которое вводил пользователь).
Функция должна:
1. Предупредить пользователя, что конечное число должно быть на 5 больше начального.
2. Попросить пользователя ввести конечное число.
3. Если пользователь ввел не число или отрицательное число, то вывести ошибку и попросить пользователя ввести число еще раз.
4. Если число не подходит (проверить через AreRightNumbers), то вывести ошибку и попросить пользователя ввести число еще раз.
5. Если число подходит, то вернуть его.
'''
from GuessTheNumber.AreRightNumbers import AreRightNumbers
from GuessTheNumber.IsPositiveNumber import IsPositiveNumber


# Это задание выполнит Никита

def GetEndNumber(StartNumber):
    print('Конечное число должно быть хотя бы на 5 больше чем стартовое')
    print('Введите конечное число')
    EndNumber = input()
    if IsPositiveNumber(EndNumber) and AreRightNumbers(StartNumber,EndNumber):
        return EndNumber
    else:
        print('Возможно вы ввели текст, отрицательное число, число большее стартового менее чем на 5 или число меньше стартового')
        return GetEndNumber(StartNumber)