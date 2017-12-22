x = [0]*10
y = []
for i in range(10):
    x[i] = int(raw_input())%42
for a in x:
    if a not in y:
        y.append(a)
print len(y)