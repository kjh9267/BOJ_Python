t = input()
for i in range(t):
    r, e, c = map(int, raw_input().split())
    if r > e - c:
        print 'do not advertise'
    elif r < e - c:
        print 'advertise'
    else:
        print 'does not matter'