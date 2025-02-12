'''
Получить начальное и конечное число.
Получить случайное число.
Запустить игру.
Поздравить пользователя с победой.
'''
# Это задание выполнит страдалец RONawht

from GuessTheNumber.GetRandomNumber import GetRandomNumber
from GuessTheNumber.GetRange import GetRange
from GuessTheNumber.Play import Play

(start, end) = GetRange()
random_number = GetRandomNumber(start, end)
Play(start, end, random_number)

print('ТЫ МОЛОДЕЦ!!!')