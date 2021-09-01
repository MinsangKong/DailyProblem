#https://www.acmicpc.net/problem/10798
#백준 10798번 세로읽기(그리디)
#import sys
#input = sys.stdin.readline

words = [list(input().rstrip()) for _ in range(5)]

result = ""

idx = 0
while True:
    flag = False
    for i in range(5):
        if idx < len(words[i]):
            result+= words[i][idx]
            flag = True
    idx+=1
    if not flag:
        print(result)
        break