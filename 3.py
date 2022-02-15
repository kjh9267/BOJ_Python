from collections import deque


def solution(pixels):
    empty_string = ''
    col_size = 3
    N = len(pixels)
    M = len(pixels[0])
    result = deque()

    number_table = {
        '111101101101111': '0',
        '110010010010111': '1',
        '111001111100111': '2',
        '111001111001111': '3',
        '101101111001001': '4',
        '111100111001111': '5',
        '111100111101111': '6',
        '111101001001001': '7',
        '111101111101111': '8',
        '111101111001111': '9'
    }

    for col_start in range(0, M, col_size):
        binaries = deque()

        for row in range(N):
            for col in range(col_start, col_start + col_size):
                binaries.append(pixels[row][col])

        number_table_key = empty_string.join(binaries)
        number = number_table[number_table_key]
        result.append(number)

    return empty_string.join(result)


if __name__ == '__main__':
    input = __import__('sys').stdin.readline
    print(solution(["111111111111111111111111110111111111","001101001101101100101101010101001100","111101111101101111101111010111111111","100101100101101101101001010101001001","111111111111111111111111111111111111"]	))
    print(solution(["110111101111111111110111","010101101100101101010100","010111111111101111010111","010001001001101101010001","111111001111111111111111"]	))
    print(solution(["111110111101111101111101","100010101101001101100101","111010111111111111111111","001010101001100001001001","111111111001111001111001"]	))
