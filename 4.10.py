n = int(input())
k = int(input())
a = 1
b = 1
position = 1
sum = 0
while n>0:
    if position>=k:
        sum += a
        n -= 1
    a = b
    b = a+b
    position += 1
print(sum)