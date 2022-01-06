#https://www.acmicpc.net/problem/20365
#백준 20365번 블로그 2 (문자열,그리디)
#import sys
#input = sys.stdin.readline

def count(target):
    cnt = 1
    if board[0] != target:
        cnt += 1
    for i in range(1,n):
        if board[i] != board[i-1]:
            if board[i] != target :
                cnt += 1
    return cnt

n = int(input())
board = list(input().rstrip())

print(min(count('B'), count('R')))