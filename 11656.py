a = raw_input()
b = [a[i:]for i in range(len(a))]
for i in range(len(b)):
    print sorted(b)[i]