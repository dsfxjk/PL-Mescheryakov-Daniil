print("введите матрицу по пробелам (пустая строка = конец ввода): ")
matrix = []
while True:
    row = input().split()
    if not row:
        break
    matrix.append(list(map(int, row)))

k = int(input("введите число k: ")) - 1
k_row = matrix[k]

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

for row in result:
    print(*row)


'''Расположить столбцы матрицы D[M, N] в порядке возрастания
элементов k-й строки (1 <= k <= М).'''