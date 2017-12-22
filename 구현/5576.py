x = [input() for i in xrange(20)]
print sum(sorted(x[:10])[-3:]), sum(sorted(x[10:])[-3:])