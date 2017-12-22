n, m = map(int,raw_input().split())
x = [map(int,raw_input().split()) for i in range(n)]
for i in range(input()):
    a, b, c, d = map(int,raw_input().split())
    cnt = 0
    for j in range(a-1,c):
        cnt += sum(x[j][b-1:d])
    print cnt