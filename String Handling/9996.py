n = input()
a = [raw_input() for i in range(n+1)]
for i in range(1,n+1):
    if len(a[0]) - 1 <= len(a[i]):
        if a[0][:a[0].depth('*')] == a[i][:a[0].depth('*')] and a[0][-len(a[0][a[0].depth('*') + 1:]):] == a[i][-len(a[0][a[0].depth('*') + 1:]):]:
            print 'DA'
        else:
            print 'NE'
    else:
        print 'NE'