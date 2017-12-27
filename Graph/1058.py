import sys

n = int(sys.stdin.readline())
graph = [0]*n
for i in range(n):
    graph[i] = list(sys.stdin.readline().rstrip())

for v in range(n):
    for i in range(n):
        for j in range(n):
            if i is not j:                                                  # 자기 자신은 친구가 아니므로 제외한다.
                if graph[i][j] is 'N':                                      # 이미 친구 관계가 아닌 사람만 검사한다.
                    if graph[i][v] is 'Y' and graph[j][v] is 'Y':           # 같은 친구를 가지고 있는 경우를 F로 표시한다.
                        graph[i][j] = 'F'

res = [i.count('Y') + i.count('F') for i in graph]                          # 이미 친구관계와 같은 친구를 가지고 있는 수
print(max(res))