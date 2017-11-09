a, b, c= raw_input().split()
n = int(a)
w = int(b)
h = int(c)
x = []

for i in range(n):
    x.append(int(raw_input()))

for i in x:
    if (w**2 + h**2) >= i**2:
        print "DA"
    else:
        print "NE"