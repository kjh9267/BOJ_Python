x = [map(int,raw_input().split()) for i in range(4)]
cnt = 0
y = [0]*4
for i in range(4):
    cnt += x[i][1] - x[i][0]
    y[i] = cnt
print max(y)