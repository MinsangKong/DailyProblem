#https://www.acmicpc.net/problem/1436
#백준 1436번 영화감독 숌 (완전탐색)
#import sys
#input = sys.stdin.readline

n = int(input())

num = 666

while True :
    if '666' in str(num):
        n -= 1
        if n == 0 :
            break
    num += 1
    
print(num)