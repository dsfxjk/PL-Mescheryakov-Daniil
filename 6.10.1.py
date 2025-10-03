num = list(map(int, input("Введите числа через пробел: ").split()))
povtor = [x for x in num if num.count(x) > 1]
if povtor:
    print("Повторяющиеся элементы: ", list(set(povtor)))
else:
    print("Повторяющиеся элементы отсутствуют")