import math

def combination(a,b):
    f = math.factorial
    return f(a)/f(a-b)/f(b)

t = input()
for i in range(t):
    n, m = map(int,raw_input().split())
    print combination(m,n)