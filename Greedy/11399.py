n = input()
x = sorted(map(int,raw_input().split()))
cnt = 0
for i in range(n):
    cnt += sum(x[:i+1])
print cnt