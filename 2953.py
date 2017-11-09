a = [sum(u) for u in [map(int,raw_input().split()) for i in range(5)]]
print a.index(max(a))+1, max(a)