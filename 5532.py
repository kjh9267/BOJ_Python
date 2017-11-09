x = [input() for i in range(5)]
for i in range(x[0]):
    x[1] -= x[3]
    x[2] -= x[4]
    if x[1]<= 0 and x[2]<=0:
        print x[0] - i -1
        break