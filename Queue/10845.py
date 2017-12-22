b = []
for i in range(input()):
    a = raw_input()
    if a[:4] == 'push':
        b.append(a[5:])
    elif a[:3] == 'pop':
        if len(b) != 0:
            print b.pop(0)
        else:
            print -1
    elif a[:4] == 'size':
        print len(b)
    elif a[:5] == 'empty':
        if len(b) == 0:
            print 1
        else:
            print 0
    elif a[:5] == 'front':
        if len(b) == 0:
            print -1
        else:
            print b[0]
    else:
        if len(b) == 0:
            print -1
        else:
            print b[-1]