n = input()
m = input()
x = [[0 for j in range(n)]for i in range(n)]
for i in range(m):
    a, b = map(int,raw_input().split())
    x[a-1][b-1] = 1
    x[b-1][a-1] = 1
visit = []
for i in range(n):
    if x[0][i] == 1 and i + 1 not in visit:
        visit.append(i + 1)
for i in range(len(visit)):
    for j in range(n):
        if x[visit[i]-1][j] == 1 and j + 1 not in visit:
            visit.append(j + 1)
print len(visit) - 1