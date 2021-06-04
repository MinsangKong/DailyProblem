#https://www.acmicpc.net/problem/9663
#백준 9663번 N-Queen(DFS,백트래킹)
#import sys
#input = sys.stdin.readline

n = int(input())

check = [0]*15 #모든 행
result = 0

def isTrue(x):
    for i in range(x):
        if check[x] == check[i] or abs(check[x]-check[i]) == x-i: #같은 열 위치 or 대각선 위치
            return False
    return True

def dfs(num):
    global result
    if num >= n:
        result += 1
    else:
        for i in range(n): #각 행에 열을 넣는 과정
            check[num] = i
            if isTrue(num) : 
                dfs(num+1) #num+1이 n과 같다면 체스 말이 모두 들어갔다는 의미
                
dfs(0)
print(result)
'''
https://blog.encrypted.gg/732 백트래킹 알고리즘 설명
'''