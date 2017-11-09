a = raw_input().split()
if a == sorted(a):
    print 'ascending'
elif a == sorted(a)[::-1]:
    print 'descending'
else:
    print 'mixed'