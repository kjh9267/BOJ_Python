n = input()
a = map(int,raw_input().split())
m = input()
d = map(int,raw_input().split())
b = sorted(d)
c = [[0 for i in range(10000001)]for j in range(2)]
e = [0]*m
for i in range(n):
    start = 0
    end = m - 1
    while start <= end:
        mid = (start + end)/2
        if b[mid] == a[i]:
            if a[i] >= 0:
                c[0][a[i]] += 1
                break
            else:
                c[1][a[i]*-1] += 1
                break
        else:
            if b[mid] > a[i]:
                end = mid - 1
            else:
                start = mid + 1
for i in range(m):
    if d[i] >= 0:
        e[i] = c[0][d[i]]
    else:
        e[i] = c[1][d[i]*-1]
print ' '.join(map(str,e))