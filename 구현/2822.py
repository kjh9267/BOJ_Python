x = [input() for i in range(8)]
y = sorted(x)[3:]
print sum(y)
z = [x.index(y[i])+1 for i in range(5)]
a = sorted(z)
b = map(str,a)
print " ".join(b)