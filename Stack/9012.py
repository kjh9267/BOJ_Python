import sys

t = int(sys.stdin.readline())
res = []
for _ in range(t):                                      # 테스트 케이스 만큼 반복
    data = list(sys.stdin.readline().strip())           # 입력받은 데이터를 리스트로
    key = False
    stack = []
    while data:
        x = data.pop()
        if x is ')':                            # 입력의 마지막 문자가 ')' 면 스택에 추가
            stack.append(x)
        else:
            if stack:                           # 입력의 마지막 문자가 '(' 일때 스택에 데이터가 있을경우 스택 pop
                stack.pop()
            else:
                res.append('NO')                # 스택에 데이터가 없을 경우 반복문 종료
                key = True
                break
    if key is True:
        continue
    if stack:                                   # 스택에 데이터가 있으면 NO
        res.append('NO')
    else:
        res.append('YES')                       # 스택이 비어있으면 YES
print("\n".join(res))