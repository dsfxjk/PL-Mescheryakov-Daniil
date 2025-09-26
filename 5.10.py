s = str(input())
slova = s.split()
for i in range(len(slova)):
    slova[i] = slova[i][0].upper() + slova[i][1:]
res = ' '.join(slova)
print(res)