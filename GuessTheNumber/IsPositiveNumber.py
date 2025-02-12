'''
Функция должна принять одну строку и проверить, является ли эта строка положительным числом.
Если да, то вернуть True.
Если нет, то вернуть False.
'''
#Это задание выполнит Айсылу

def IsPositiveNumber(string):
    countof0 = string.count('0')
    countof1 = string.count('1')
    countof2 = string.count('2')
    countof3 = string.count('3')
    countof4 = string.count('4')
    countof5 = string.count('5')
    countof6 = string.count('6')
    countof7 = string.count('7')
    countof8 = string.count('8')
    countof9 = string.count('9')
    sumcounts = countof0 + countof1 + countof2 + countof3 + countof4 + countof5 + countof6 +countof7 + countof8 + countof9
    if len(string) == sumcounts and string[0] != '0':
        return True
    else:
        return False