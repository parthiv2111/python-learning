# https://www.hackerrank.com/challenges/text-wrap/problem?isFullScreen=true

import textwrap


def wrap(string, max_width):
    result = []
    start_idx, end_idx = 0, max_width

    while start_idx < len(string):
        result.append(string[start_idx:end_idx])
        start_idx += max_width
        end_idx += max_width

    return "\n".join(result)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)
