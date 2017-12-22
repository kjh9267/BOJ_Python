a = map(int,raw_input().split())
b = map(int,raw_input().split())
if sum(a) >= sum(b):
    print sum(a)
else:
    print sum(b)