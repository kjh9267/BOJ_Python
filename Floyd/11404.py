n = input()
m = input()
x = [[10000000 for u in range(n)]for i in range(n)]
for i in range(len(x)):
    x[i][i] = 0
for i in range(m):
    a, b, c = map(int,raw_input().split())
    x[a-1][b-1] = min(c, x[a-1][b-1])
for i in range(n):
    for u in range(n):
        for o in range(n):
            x[u][o] = min(x[u][o], x[u][i] + x[i][o])
for i in range(len(x)):
    for u in range(len(x)):
        x[i][u] = str(x[i][u])
for i in range(len(x)):
    print " ".join(x[i])