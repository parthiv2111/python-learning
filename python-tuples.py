# https://www.hackerrank.com/challenges/python-tuples
# works only with python2 version

if __name__ == '__main__':
    n = int(raw_input())
    integer_list = map(int, raw_input().split())
    print(hash(tuple(integer_list)))
