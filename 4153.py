while True:
    x = sorted(map(int,raw_input().split()))
    if sum(x) == 0:
        break
    if x[0]**2 + x[1]**2 == x[2]**2:
        print 'right'
    else:
        print 'wrong'
