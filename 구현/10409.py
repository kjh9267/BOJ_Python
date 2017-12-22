n, t = map(int,raw_input().split())
a = map(int,raw_input().split())
cnt, b = 0, 0
for i in range(len(a)):
    if cnt + a[i] <= t:
        cnt += a[i]
        b += 1
    else:
        break
print b