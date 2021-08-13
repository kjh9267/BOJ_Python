# https://www.acmicpc.net/problem/1059

if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    L = int(input())
    data = [0] + list(sorted(map(int, input().split())))
    n = int(input())

    left_count = 0
    right_count = 0
    prev_number = data[0]
    result = 0

    for index in range(L):
        left_number = data[index]
        right_number = data[index + 1]

        if left_number < n < right_number:
            left_count = n - left_number - 1
            right_count = right_number - n - 1

    result += left_count * right_count + left_count
    result += right_count

    print(result)
