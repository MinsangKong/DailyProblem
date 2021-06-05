#https://www.acmicpc.net/problem/18511
#백준 18511번 큰 수 구성하기(DFS,그리디)
#import sys
#input = sys.stdin.readline
from itertools import product

N,K = map(int,input().split())
arr = list(map(str,input().split()))
length = len(str(N))

while(True):
    temp = list(product(arr, repeat=length))
    answer = []

    for i in temp :
        if int("".join(i)) <= N :
            answer.append(int("".join(i)))

    if len(answer)>= 1:
        print(max(answer))
        break
    else : 
        length -=1
'''
dfs를 활용하거나 product로 계산하는 방식만 정답으로 처리되는 신기한 문제...
'''