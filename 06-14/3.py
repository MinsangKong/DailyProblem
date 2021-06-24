#https://www.acmicpc.net/problem/2224
#백준 2224번 명제 증명(플로이드)
#import sys
#input = sys.stdin.readline

n = int(input())

visited = [[0]*52 for _ in range(52)]

cnt = 0

for i in range(52):
    visited[i][i] = 1
    
for _ in range(n):
    data = input().split()
    for i in [0, 2]:
        data[i] = ord(data[i])
        if ord("a") <= data[i] <= ord("z"):
            data[i] = data[i] - ord("a") + 26
        else:
            data[i] = data[i] - ord("A")
    if visited[data[0]][data[2]] == 0:
        cnt += 1
        visited[data[0]][data[2]] = 1

for k in range(52):
    for i in range(52):
        for j in range(52):
            if i == j:
                continue
            if visited[i][k] == 1 and visited[k][j] == 1 and visited[i][j] == 0:
                cnt+=1
                visited[i][j] = 1
                
print(cnt)
for i in range(52):
    for j in range(52):
        if i != j and visited[i][j] == 1:
            if 0 <= i < 26:
                s = chr(ord('A')+i)
            else:
                s = chr(ord('a')+i - 26)
            if 0 <= j < 26:
                e = chr(ord('A')+j)
            else:
                e = chr(ord('a')+j - 26)
            print("%c => %c" %(s,e))