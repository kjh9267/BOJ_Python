x = [list(raw_input())[0] for i in range(input())]
z = []
for y in set(x):
    if x.count(y) > 4:
        z.append(y)
if len(z) != 0:
    print "".join(sorted(z))
else:
    print "PREDAJA"