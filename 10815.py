n = input()
a = map(int,raw_input().split())
m = input()
b = map(int,raw_input().split())
c = set(a).intersection(set(b))
d = []
for i in range(len(b)):
    if b[i] in c:
        d.append('1')
    else:
        d.append('0')
print " ".join(d)