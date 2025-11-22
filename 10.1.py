f = open("Mescheryakov-D_уб51_vvod.txt", 'r')
matrix = [list(map(int, line.split())) for line in f]
f.close()

max_val = 0

for row in matrix:
    if row == sorted(row) or row == sorted(row)[::-1]:
        row_max = max(row)
        if max_val == 0 or row_max > max_val:
            max_val = row_max

f = open("Mescheryakov-D_уб51_vivod.txt", 'w')
f.write(str(max_val) if max_val != 0 else "Нет отсортированных строк")
f.close()