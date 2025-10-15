def prost(n):
    if n<2:
        return False
    if n == 2:
        return True
    if n%2 == 0:
        return False
    for i in range(3, int(n**0.5)+1, 2):
        if n%i == 0:
            return False
    return True

n = int(input("n: "))

for num in range(2, n+1):
    if prost(num):
        binn = bin(num)[2:]
        if binn == binn[::-1]:
            print(num , "=" , binn)

'''Найти все простые натуральные числа, не превосходящие n, двоичная запись
которых представляет собой палиндром, т. е. читается одинаково слева
направо и справа налево.'''