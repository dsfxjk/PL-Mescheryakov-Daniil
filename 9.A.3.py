def reverse(n):
    if n < 10:
        print(n)
    else:
        print(n % 10, end="")
        reverse(n // 10)

num = int(input("Введите число: "))
reverse(num)


'''Вывести число в обратном порядке'''