"""
3. Реализовать функцию my_func(), которая принимает три позиционных аргумента,
и возвращает сумму наибольших двух аргументов.
Попробуйте решить задачу двумя способами:
1) используя функцию sort()
2) без функции sort()
"""


def sum_sort(*args):
    return sum(sorted(args)[-2:])


def sum_no_sort(*args):
    return sum(args) - min(args)


print(f"Результат с сортировкой: {sum_sort(5, 2, 3)}")
print(f"Результат без сортировки: {sum_no_sort(1, 2, 3)}")
