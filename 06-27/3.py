#https://www.acmicpc.net/problem/11047
#백준 11047번 동전 0(그리디)
#import sys
#input = sys.stdin.readline

n, k = map(int, input().split())

coins = [int(input()) for _ in range(n)]

cnt = 0

while k > 0:
    coin = coins.pop()
    cnt+=k//coin
    k %=coin
print(cnt)