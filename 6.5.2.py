spisok = list(map(int, input("Введите 10 чисел через пробел: ").split()))

if len(spisok) != 10:
    print("Надо ввести 10 чисел")
else:
    print(list(set(spisok)))