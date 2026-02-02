# https://www.hackerrank.com/challenges/string-validators

if __name__ == '__main__':
    s = input()
    alphanumeric, alphabetical, digits, lowercase, uppercase = 0, 0, 0, 0, 0

    for char in s:
        if char.isalnum():
            alphanumeric += 1
        if char.isalpha():
            alphabetical += 1
        if char.isdigit():
            digits += 1
        if char.islower():
            lowercase += 1
        if char.isupper():
            uppercase += 1
    print("True" if alphanumeric > 0 else "False")
    print("True" if alphabetical > 0 else "False")
    print("True" if digits > 0 else "False")
    print("True" if lowercase > 0 else "False")
    print("True" if uppercase > 0 else "False")
