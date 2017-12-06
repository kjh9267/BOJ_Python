import sys
res = ''
a = [sys.stdin.readline().strip() for i in xrange(5)]
for i in xrange(15):
    for j in xrange(5):
        try:
            res += a[j][i]
        except:
            pass
print res