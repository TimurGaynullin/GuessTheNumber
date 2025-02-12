'''
Функция не принимает никакие параметры.
Функция должна получить начальное число, конечно число и вернуть их в массиве из двух чисел. Например, [1, 10]
'''
from GetEndNumber import GetEndNumber
from GetStartNumber import GetStartNumber


# Это задание выполнит ...

def GetRange():
    a = GetStartNumber()
    b = GetEndNumber()
    return [a, b]