spisok = list(map(int, input("Введите 15 чисел через пробел: ").split()))

if len(spisok) != 15:
    print("Надо ввести 15 чисел")
else:
    print("Первоначальный массив:", spisok)
    for i in range(len(spisok)):
        if spisok[i] < 10:
            spisok[i] = 0
        elif spisok[i] > 20:
            spisok[i] = 1
    print("Преобразованный массив:", spisok)