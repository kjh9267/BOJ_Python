import sys
a, b = sys.stdin.readline().strip().split()
graph = [['.' for j in xrange(len(a))] for i in xrange(len(b))]
for i, j in enumerate(a):
    if j in b:
        c = i
        d = b.index(j)
        break
graph[d] = list(a)
for i, j in enumerate(graph):
    j[c] = b[i]
print "\n".join(map("".join,graph))