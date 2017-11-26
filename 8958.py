for i in range(input()):
    cnt = 0
    a = 0
    for j in raw_input():
        if j == 'O':
            cnt += 1 + a
            a += 1
        else:
            a = 0
    print cnt