x = input()
y = []
z = []
a, b, c, d, e = raw_input().split()
for i in [a,b,c,d,e]:
    if int(i) == x:
        z.append(i)
print len(z)