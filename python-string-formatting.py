# https://www.hackerrank.com/challenges/python-string-formatting

def print_formatted(number):
    width = len(format(number, 'b'))

    for i in range(1, number + 1):
        dec = str(i).rjust(width)
        octal = format(i, 'o').rjust(width)
        hexa = format(i, 'X').rjust(width)
        binary = format(i, 'b').rjust(width)

        print(dec, octal, hexa, binary)


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
