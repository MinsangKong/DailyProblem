#https://www.acmicpc.net/problem/1342
#백준 1342번 행운의 문자열(문자열, DFS, 순열)
#import sys
#input = sys.stdin.readline

def factorial(num):
    result = 1
    for i in range(num,0,-1):
        result *= i
    return result

def dfs(idx):
    global cnt
    if idx == length:
        for i in range(1, length):
            if temp[i-1] == temp[i]:
                return
        cnt += 1
        return
    for i in range(length):
        if not visited[i]:
            visited[i] = 1
            temp[idx] = word[i]
            dfs(idx+1)
            visited[i]=0

word = input().rstrip()
length = len(word)
alphas = [0]*26
cnt = 0

for i in range(length):
    alphas[ord(word[i])-ord('a')] += 1
    
visited = [0]*length
temp = list(word[:])
if length == len(set(word)):
    print(factorial(length))
else:
    dfs(0)

    for i in range(26):
        if alphas[i] > 1 :
            cnt //= factorial(alphas[i])

    print(cnt)