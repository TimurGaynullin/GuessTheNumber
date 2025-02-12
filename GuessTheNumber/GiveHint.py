'''
Функция должна принять два числа (число пользователя и ответ).
Вывести подсказку (число пользователя больше или меньше ответа).
'''
# Это задание выполнит тоже RONawht


def GiveHint(personalNum, answerNum):
    if personalNum > answerNum:
        print('загаданное число меньше')
    if personalNum < answerNum:
        print('загаданное число больше')