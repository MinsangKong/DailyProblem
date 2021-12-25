#https://www.acmicpc.net/problem/2204
#백준 2204번 도비의 난독증 테스트(문자열)
#import sys
#input = sys.stdin.readline

while True:
    n = int(input().rstrip())
    if n == 0:
        break
    arr = []
    for i in range(n):
        word = input().rstrip()
        arr.append((word.lower(), word))
    arr.sort()
    print(arr[0][1])