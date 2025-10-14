def find(a,b,c,N):
    count = 0
    digit_set = {str(a), str(b), str(c)}
    for i in range(100, N+1):
        number = str(i)
        if all(x in digit_set for x in number):
            count += 1
    return count

print("введите 3 числа")
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
print("введите значение N (210 < N < 231): ")
N = int(input("N: "))

print("результат: ", find(a,b,c,N))


'''На отрезке [100, N] (210 < N < 231) найти количество чисел, составленных из
цифр а, b, с'''