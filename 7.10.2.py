string = input("Введите текст: ")

def reverse_string(s):
    words = s.split()
    reversed_string = words[::-1]
    return " ".join(reversed_string)

print(reverse_string(string))

'''Составить программу, которая изменяет последовательность слов в строке на
обратную.'''