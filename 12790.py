x = [map(int,raw_input().split()) for i in range(input())]
for i in x:
    if i[0] + i[4] < 1:
        i[4] = 1
        i[0] = 0
    if i[1] + i[5] < 1:
        i[5] = 1
        i[1] = 0
    if i[2] + i[6] < 0:
        i[6] = 0
        i[2] = 0
    print i[0] + i[1] * 5 + i[2] * 2 + i[3] * 2 + i[4] + i[5] * 5 + i[6] * 2 + i[7] * 2