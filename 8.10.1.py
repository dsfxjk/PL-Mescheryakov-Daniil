print("введите матрицу по пробелам (пустая строка = конец ввода): ")
matrix = []
while True:
    row = input().split()
    if not row:
        break
    matrix.append(list(map(int, row)))

max_val = 0

for row in matrix:
    if row == sorted(row) or row == sorted(row)[::-1]:
        row_max = max(row)
        if max_val == 0 or row_max > max_val:
            max_val = row_max

print(max_val if max_val != 0 else "Нет отсортированных строк")


'''Найти максимальный среди всех элементов тех строк заданной
матрицы, которые упорядочены (либо по возрастанию, либо по
убыванию).'''