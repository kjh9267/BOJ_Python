for i in range(3):
    x = map(int, raw_input().split())
    a = x[0] * 3600 + x[1] * 60 + x[2]
    b = x[3] * 3600 + x[4] * 60 + x[5]
    c = b - a
    h = c/3600
    m = (c - h*3600)/60
    s = (c - h*3600 - m*60)
    print h, m, s