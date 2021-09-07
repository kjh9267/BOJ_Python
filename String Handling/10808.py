a = raw_input()
x = []
for i in range(97,123):
    x.append(str(a.depth(chr(i))))
print " ".join(x)