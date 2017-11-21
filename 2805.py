n, m = map(int,raw_input().split())
x = map(int,raw_input().split())
first = 0
last = max(x)
y = []
z = []
while first <= last:
    a = [0]*len(x)
    for i in range(len(x)):
        a[i] = x[i]
    mid = (first + last)/2
    for i in range(len(a)):
        if a[i] > mid:
            a[i] -= mid
        else:
            a[i] = 0
    if sum(a) >= m:
        y.append(abs(sum(a) - m))
        z.append(mid)
        first = mid + 1
    else:
        last = mid - 1
print z[y.index(min(y))]