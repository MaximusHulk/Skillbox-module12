print('Задача 1. Сумма чисел')


def summa_n():
    summ = 0
    for numbers in range(1, number + 1):
        summ = numbers + summ
    print('Я знаю, что сумма чисел от 1 до', number, ' равна', summ)


number = int(input('Введите число до которого нужно посчитать сумму: '))
summa_n()
# Напишите функцию summa_n,
# которая принимает одно целое положительное число N
# и выводит сумму всех чисел от 1 до N включительно.
#
# Пример работы программы:
# Введите число: 5
#
# Я знаю, что сумма чисел от 1 до 5 равна 15
