t = input()
for y in range(t):
    n = input()
    a, b = [0] * n, [0] * n
    for i in range(n):
        c, g = raw_input().split()
        a[i] = int(c)
        b[i] = float(g)*int(c)
    print "{} {}".format(sum(a),round(sum(b)/sum(a),1))

