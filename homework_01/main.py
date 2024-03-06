"""
Домашнее задание №1
Функции и структуры данных
"""

def power_numbers(*numbers):

    for number in numbers:
        print(number ** 2)

power_numbers(1, 4, 6, 3)

    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """


# filter types
def is_odd(*numbers):
    for number in numbers:
      if number % 2 == 0:
        print(number)

def is_even(*numbers):
    for number in numbers:
      if number % 2 == 1 or number == 1:
        print(number)

def is_prime(number):
    for n in range(2, number):
      if number % n == 0:
        return False
    print(number)


ODD = "odd"
EVEN = "even"
PRIME = "prime"

def filter_numbers(*numbers, type):
    if type == ODD:
        is_odd(*numbers)
    elif type == EVEN:
        is_even(*numbers)
    elif type == PRIME:
        for number in [*numbers]:
            is_prime(number)

filter_numbers(1,3,4,5,67,34,2,2, type=PRIME)

    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    """
