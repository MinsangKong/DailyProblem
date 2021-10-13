import sys


def palindrome(num, length):
    s = str(num).zfill(length)
    return s == s[::-1]


def main():
    for line in sys.stdin:
        n, length = int(line), len(line) - 1
        if n == 0 and length == 1:
            break
        x = 0
        while not palindrome(n + x, length):
            x += 1
        print(x)


main()