n = input()
x = [map(int,raw_input().split()) for i in range(n)]
for i in range(n):
    for u in range(n):
        for o in range(n):
            if x[u][o] == 1:
                x[u][o] = 1
            if x[u][i] == 1 and x[i][o] == 1:
                x[u][o] = 1
for i in range(len(x)):
    for u in range(len(x)):
        x[i][u] = str(x[i][u])
for i in range(len(x)):
    print " ".join(x[i])