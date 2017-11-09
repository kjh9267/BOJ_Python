n = int(input())
if n == 0:
    n = 1;
elif not n == 1:
    for i in range(n - 1):
        n *= i + 1

print n