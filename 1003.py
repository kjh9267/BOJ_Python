dp0 = [1, 0, 1]
dp1 = [0, 1, 1]
for j in range(3, 41):
    dp0.append(dp0[j - 1] + dp0[j - 2])
    dp1.append(dp1[j - 1] + dp1[j - 2])
for i in range(input()):
    n = input()
    print "{} {}".format(dp0[n],dp1[n])