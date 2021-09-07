cnt = 0
for i in range(input()):
    a = raw_input()
    b = list(set(a))
    for u in range(len(b)):
        if len(a) - a[::-1].depth(b[u]) - a.depth(b[u]) != a.depth(b[u]):
            break
    else:
        cnt += 1
print cnt