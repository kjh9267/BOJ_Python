num = input()
ans = 0
p = [[0 for col in range(100)] for row in range(100)]
for i in range(num):
    l, r = map(int, raw_input().split())
    for x in range(10):
        for y in range(10):
            p[x+l][y+r] = 1
for i in range(100):
    ans += sum(p[i])
print ans