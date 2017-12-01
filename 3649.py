while True:
    x = int(input()) * 10000000
    n = int(input())
    a = [int(input()) for i in range(n)]
    b = []
    c = {}
    for i in range(n):
        for j in range(i+1,n):
            b.append(a[i] + a[j])
            if c.has_key(a[i]+a[j]):
                c[a[i]+a[j]][(a[i],a[j])] = abs(a[i]-a[j])
            else:
                c[a[i]+a[j]] = {}
                c[a[i] + a[j]][(a[i], a[j])] = abs(a[i] - a[j])
    b = sorted(b)
    first = 0
    last = len(b) - 1
    while first <= last:
        mid = (first+last)/2
        if b[mid] == x:
            for i, j in c[b[mid]].items():
                if max(c[b[mid]].values()) == j:
                    print 'yes ' + ' '.join(map(str, sorted(i)))
            break
        else:
            if b[mid] > x:
                 last = mid - 1
            else:
                first = mid + 1
    else:
        print 'danger'