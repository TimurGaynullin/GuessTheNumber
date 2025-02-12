'''
Получить начальное и конечное число.
Получить случайное число.
Запустить игру.
Поздравить пользователя с победой.
'''
# Это задание выполнит страдалец RONawht

from GetRandomNumber import GetRandomNumber
from GetRange import GetRange
from Play import Play

(start, end) = GetRange()
random_number = GetRandomNumber(start, end)
Play(start, end, random_number)

print('ТЫ МОЛОДЕЦ!!!')