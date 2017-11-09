a, b ,c = map(int,raw_input().split())
cnt = (a+b)/c
empty = (a+b)/c + (a+b)%c
while empty/c >= 1:
    cnt += empty/c
    empty = empty/c + empty%c
print cnt