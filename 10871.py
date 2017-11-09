n, x =map(int,raw_input().split())
l = map(int,raw_input().split())
y = [str(l[i]) for i in range(n) if l[i] < x]
print " ".join(y)
