x = [0]*5
for i in range(5):
    x[i] = int(raw_input())
print min(x[0]*x[4],x[1]+max(x[4]-x[2],0)*x[3])