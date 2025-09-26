n = int(input())
k = int(input())
a = 1
b = 1
sum = 0
for i in range(k+n-1):
    if i >= k-1:
        sum += a
    a = b
    b = a+b
print(sum)