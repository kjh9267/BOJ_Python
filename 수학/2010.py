import sys
n = input()
cnt = 0
for i in range(n):
    cnt += int(sys.stdin.readline())
print cnt - n + 1