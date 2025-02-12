'''
Функция должна принять три числа (начальное число, конечное число и ответ).
1. Сообщить пользователю, в каком промежутке было загадано число.
2. Попросить ввести число.
3. Если введено не число, или не в том промежутке, или не верное, дать подсказку и предложить ввести число еще раз.
4. Если число угадано, завершить выполнение функции.
'''
from GiveHint import GiveHint
from IsNumberInSegment import IsNumberInSegment
from IsPositiveNumber import IsPositiveNumber


# Это задание выполнит Акмаль


def Play(start, end, answer):
    IsVictory = False
    print(f'Мы загадали число от {start} до {end}. Отгадайте его!')
    while not IsVictory:
        print('Какое число мы загадали?')
        number = input()
        if IsPositiveNumber(number):
            number = int(number)
            if IsNumberInSegment(start, end, answer):
                if number == answer:
                    IsVictory = True
                else:
                    GiveHint(number, answer)
            else:
                print(f'Это число не входит в отрезок от {start} до {end}. Попробуйте еще раз')

        else:
            print('Необходимо ввести положительное число (без знака минус и других символов). Попробуйте еще раз')