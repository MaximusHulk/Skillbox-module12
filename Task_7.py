print('Задача 7. Опять?')
def search_min_number():
    x = int(input('Введи число: '))
    y = int(input('Введи число: '))
    b = ((x + y) - abs(x - y)) // 2
    print('минимальное число: ', b)

search_min_number()
# Вы снова встретились со своим старым другом,
# который был безмерно благодарен вам за то,
# что вы помогли ему сдать задачу тому преподавателю.
#
# Вот только друг всё равно выглядел довольно грустным.
# Спросив в чём дело, друг взорвался эмоциями и рассказал,
# что теперь препод попросил написать функцию нахождения минимального числа
# без использования условного оператора, циклов и функции min.
#
# Конечно же, вы решили снова помочь бедняге.
# Напишите для него такую программу.