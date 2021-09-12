"""
Домашнее задание №1
Функции и структуры данных
"""


def power_numbers(*args):
    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    return [x * x for x in args]


# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"
out_ls = []

def filter_numbers(ls, args=None):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
    if args == ODD:
        return [x for x in ls if x % 2 != 0]
    elif args == EVEN:
        return [x for x in ls if x % 2 == 0]

    elif args == PRIME:
        for i in range(len(ls)):
            k = 0

            for n in range(1,i+1):
                if i % n == 0:
                    k +=1

            if k == 2:
                out_ls.append(i)
        return out_ls

