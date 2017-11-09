x = []
for i in range(5):
    y = int(raw_input())
    x.append(y)
print min(x[:3]) + min(x[3:]) - 50