spisok = list(map(int, input("Введите 10 чисел через пробел: ").split()))

if len(spisok) != 10:
    print("Надо ввести 10 чисел")
else:
    for i in range(len(spisok) - 1):
        if spisok[i] < 0  and spisok[i+1] < 0:
            print(spisok[i], spisok [i+1])
