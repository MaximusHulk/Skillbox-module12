print('Задача 3. Апгрейд калькулятора')


def main_menu():
    number = int(input('Введи число : '))

    def summ(number):
        count = 0
        new_summ = 0
        while number > 0:
            count = number % 10 + count
            new_summ = count + new_summ
            count = 0
            number //= 10
        print(new_summ)
        main_menu()

    def max(number):
        biggernumber = 0
        big = 0
        for numbers in number:
            if int(numbers) >= biggernumber:
                biggernumber += int(numbers)
                if biggernumber > big:
                    big = biggernumber
            biggernumber = 0
        print(big)
        main_menu()

    def mini(number):
        smaller = 9
        small = 9
        for numbers in number:
            if int(numbers) <= smaller:
                smaller = 0
                smaller += int(numbers)
                if smaller < small:
                    small = 0
                    small += smaller
            smaller = 9
        print(small)
        main_menu()

    task = input('1 - вывести сумму, 2 - вынести максимальную цифру, 3 - минимальную: ')
    if task == '1':
        summ(number)
    elif task == '2':
        max(str(number))
    elif task == '3':
        mini(str(number))


main_menu()


# Степан, как и большая часть населения планеты,
# для расчёта суммы и разности чисел использует калькулятор.
#
# Однако в работе ему нужно
# делать не только  обычные действия вроде сложения и вычитания,
# а делать что-то вручную он уже устал.
#
# Поэтому Степан решил немного расширить функциональность своего калькулятора.
#
# Напишите программу,
# которая спрашивает у пользователя число и действие,
# которое нужно с ним сделать:
# вывести сумму его цифр,
# вывести максимальную цифру или вывести минимальную цифру.
#
# Каждое действие оформите в виде отдельной функции,
# а основную программу зациклите.