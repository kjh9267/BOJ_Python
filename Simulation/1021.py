def left(queue):
    queue.append(queue[0])
    queue.pop(0)
def right(queue):
    queue.insert(0,queue[-1])
    queue.pop(-1)
n, m = map(int,raw_input().split())
x = map(int,raw_input().split())
queue = range(1,n+1)
plist = []
cnt = 0
for i in range(m):
    while x[i] not in plist:
        if queue[0] == x[i]:
            plist.append(queue.pop(0))
        else:
            if queue.index(x[i]) <= len(queue)/2:
                for j in range(queue.index(x[i])):
                    left(queue)
                    cnt += 1
            else:
                for j in range(len(queue) - queue.index(x[i])):
                    right(queue)
                    cnt += 1
print cnt