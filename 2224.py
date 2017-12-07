import sys
n = int(sys.stdin.readline())
inf = float('inf')
graph = [[inf for j in range(52)] for i in range(52)]
for i in xrange(n):
    a, _, b = sys.stdin.readline().strip().split()
    if a is not b:
        if ord(a) <= 90:
            a = ord(a) - 65
        else:
            a = ord(a) - 71
        if ord(b) <= 90:
            b = ord(b) - 65
        else:
            b = ord(b) - 71
        graph[a][b] = 1
for v in xrange(52):
    for i in xrange(52):
        for j in range(52):
            if i is not j:
                if graph[i][v] + graph[v][j] is 2:
                    graph[i][j] = 1
print sum([i.count(1) for i in graph])
for i in xrange(26):
    for j in xrange(52):
        if graph[i][j] is 1:
            if j <= 25:
                print chr(i + 65), '=>', chr(j + 65)
            else:
                print chr(i + 65), '=>', chr(j + 71)
for i in xrange(26,52):
    for j in xrange(52):
        if graph[i][j] is 1:
            if j <= 25:
                print chr(i + 71), '=>', chr(j + 65)
            else:
                print chr(i + 71), '=>', chr(j + 71)