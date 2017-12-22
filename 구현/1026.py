n = input()
a = sorted(map(int,raw_input().split()))
b = sorted(map(int,raw_input().split()))[::-1]
cnt = 0
for i in range(n):
    cnt += a[i] * b[i]
print cnt