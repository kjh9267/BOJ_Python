n = 1000 - input()
cnt = 0
while n != 0:
    if n >= 500:
        n -= 500
        cnt += 1
    if n >= 100:
        n -= 100
        cnt += 1
        continue
    if n >= 50:
        n -= 50
        cnt += 1
        continue
    if n >= 10:
        n -= 10
        cnt += 1
        continue
    if n >= 5:
        n -= 5
        cnt += 1
        continue
    if n >= 1:
        n -= 1
        cnt += 1
print cnt