input()
a = map(int,raw_input().split())
input()
b = map(int,raw_input().split())
c = set(a).intersection(set(b))
for i in b:
    if i in c:
        print 1
    else:
        print 0