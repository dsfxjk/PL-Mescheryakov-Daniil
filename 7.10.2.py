stringi = input("Введите текст: ")

def reverse_stringi(s):
    words = s.split()
    reversed_stringi = words[::-1]
    return " ".join(reversed_stringi)

print(reverse_stringi(stringi))

'''Составить программу, которая изменяет последовательность слов в строке на
обратную.'''