def solution(game_history):
    result = 0
    score = 0

    for diff in game_history:
        score += diff
        if score > 0:
            result += 1

    return result


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    print(solution([ 5, 2, -16, 4 ]	))
    print(solution([-1, 1, -1]))
    print(solution([-1, 1, 1]))

    import time

    listt = list(range(100_000_000))
    start = time.time()

    print(solution(listt))

    print(time.time() - start)
