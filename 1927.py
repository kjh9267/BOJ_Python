import heapq
import sys

n = int(sys.stdin.readline())
heap = []
for i in xrange(n):
    a = int(sys.stdin.readline())
    if a is 0:
        if heap:
            print heapq.heappop(heap)
        else:
            print 0
    else:
        heapq.heappush(heap,a)