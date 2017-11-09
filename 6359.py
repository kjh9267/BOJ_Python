x = [[1 for _ in range(input())] for i in range(input())]
for i in range(len(x)):
    for y in range(1,len(x[i])):
        for u in range(y,len(x[i]),y+1):
            if x[i][u] == 0:
                x[i][u] = 1
            else:
                x[i][u] = 0
for i in x:
    print sum(i)