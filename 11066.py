t = input()
for i in range(t):
    k = input()
    l = map(int,raw_input().split())
    while len(l) != 1:
        if len(l)%2 == 0:
            for u in range(0,len(l),2):
                l[u] = ((l[u]) + (l[u+1]))
                l[u+1] = 0
                print l
        else:
            for u in range(0,len(l)-1,2):
                l[u] = ((l[u]) + (l[u+1]))
                l[u+1] = 0
                print l
        l = sorted(l)
        del l[:l.count(0)]
        print l