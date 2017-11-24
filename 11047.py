n, k = map(int,raw_input().split())
x = [input() for i in range(n)]
cnt = 0
for i in range(n-1,-1,-1):
    cnt += k/x[i]
    k %= x[i]
print cnt