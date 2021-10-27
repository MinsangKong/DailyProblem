import sys


def main():
    n, a, b, c, d = (int(x) for x in sys.stdin.readline().split())
    ans = 10 ** 100
    for x in range(min(c, n // a + 1)):
        y = (n - a * x - 1) // c + 1
        ans = min(ans, b * x + d * y)
    for y in range(min(a, n // c + 1)):
        x = (n - c * y - 1) // a + 1
        ans = min(ans, b * x + d * y)
    print(ans)


main()