#https://www.acmicpc.net/problem/10597
#백준 10597번 순열장난(DFS, 백트래킹)
import sys
#input = sys.stdin.readline

def dfs(idx, cnt):
    if cnt == result:
        for i in range(len(num)):
            print(num[i], end = " ")
        sys.exit(0)
    
    for i in range(1,3):
        target = int(nums[idx:idx+i])
        if target <= result and not visited[target]:
            num.append(target)
            visited[target] = 1
            dfs(idx+i,cnt+1)
            visited[target] = 0
            num.pop()
        
nums = input().rstrip()
length = len(nums)
temp = length
result = 0
num = []

if temp <= 9 :
    result = length
else:
    result += 9
    temp -= 9
    result += temp//2
    
visited = [0]*(result+1)
visited[0] = 1
dfs(0,0)
#visited[0]을 제대로 처리 안해서 발생한 오류... 후 테스트케이스를 하나하나 하다가 알아냄 
#화가 너무 난다...