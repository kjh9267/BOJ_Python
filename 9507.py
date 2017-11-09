t = input()
x = [1,1,2,4]
for i in range(4,68):
    x.append(x[i-1] + x[i-2] + x[i-3] + x[i-4])
for i in range(t):
    print x[input()]