f = open("Mescheryakov-D_уб51_vvod2.txt", 'r')
lines = f.readlines()
f.close()

matrix = [list(map(int, line.split())) for line in lines[:-1]]

k = int(lines[-1])
k_row = matrix[k - 1]

'''создаем список пар и сортируем'''
pairs = []
for i in range(len(k_row)):
    pairs.append((k_row[i], i))
pairs.sort()

'''извлекаем отсортированные индексы'''
indexes = []
for pair in pairs:
    indexes.append(pair[1])

'''новая матрица с изменениями'''
result = []
for row in matrix:
    new_row = []
    for i in indexes:
        new_row.append(row[i])
    result.append(new_row)

f = open("Mescheryakov-D_уб51_vivod2.txt", 'w')
for row in result:
    f.write(' '.join(map(str, row)) + '\n')
f.close()


'''Для заданий из практической работы №8 для своего варианта.
Организовать ввод данных (матриц) из файла (имя: ФИО_группа_vvod.txt)
И вывод результатов в файл (имя: ФИО_группа_vivod.txt)'''

'''Расположить столбцы матрицы D[M, N] в порядке возрастания
элементов k-й строки (1 <= k <= М).'''