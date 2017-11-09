a = list(raw_input())
b = list(raw_input())
c = list(raw_input())
d = list(raw_input())
e = list(raw_input())
z = [a,b,c,d,e]
x = []
for i in range(15):
    for y in z:
        try:
            x.append(y[i])
        except:
            continue
print "".join(x)