def find_second_max(first=None, second=None):
    num = int(input())
    if num == 0:
        return second
    if first is None or num > first:
        return find_second_max(num, first)
    if second is None or num > second:
        return find_second_max(first, num)
    return find_second_max(first, second)

num = int(input())
print(find_second_max(num) if num != 0 else None)


'''Дана последовательность натуральных чисел (одно число в строке),
завершающаяся числом 0. Определите значение второго по величине
элемента в этой последовательности, то есть элемента, который будет
наибольшим, если из последовательности удалить наибольший элемент.
'''