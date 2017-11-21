def stack(a, arg):
    if arg[0] == 'push':
        a.append(arg[1])
    elif arg[0] == 'pop':
        if len(a) == 0:
            print -1
        else:
            print a.pop(len(a)-1)
    elif arg[0] == 'size':
        print len(a)
    elif arg[0] == 'empty':
        if len(a) == 0:
            print 1
        else:
            print 0
    else:
        if len(a) != 0:
            print a[len(a)-1]
        else:
            print -1
    return a
b = []
for i in range(input()):
    stack(b, raw_input().split())