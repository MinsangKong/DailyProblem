#https://www.acmicpc.net/problem/15661
#백준 15661번 링크와 스타트 (완전탐색)
import sys
#input = sys.stdin.readline
from itertools import combinations

def count(index):
    start = 0
    link = 0
    for i in range(n):
        for j in range(i+1,n):
            if i in index and j in index :
                start += status[i][j]+status[j][i]
            elif i not in index and j not in index :
                link += status[i][j]+status[j][i]
    return abs(start-link)
    
n = int(input())
status = [list(map(int, input().split())) for _ in range(n)]
result = int(1e9)
limit = n//2+1
nums = [i for i in range(n)]
for i in range(1, limit):
    for case in combinations(nums, i):
        index = dict()
        for idx in case:
            index[idx] = 1
        result = min(count(index),result)
        if result == 0 :
            print(result)
            sys.exit(0)

print(result)
#재귀 방식으로는 무조건 시간초과와 메모리 초과 발생
#따라서 combinations 함수를 통해 반복형태로 구현하는 것이 일반적인 해답
