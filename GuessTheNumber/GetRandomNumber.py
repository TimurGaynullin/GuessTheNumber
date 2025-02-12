'''
Функция должна принять два числа (начальное число и конечное).
А затем вернуть случайное целое число в промежутке от начального до конечного.
Как получить случайное число, можно узнать в интернете
'''
# Это задание выполнит RONawht
import random
def GetRandomNumber(first_number, ended_number):
    return random.randint(first_number, ended_number)