#https://www.acmicpc.net/problem/15664
#백준 15664번 N과 M (10) (DFS, 백트래킹)
#import sys
#input = sys.stdin.readline

def dfs(idx, number,cnt):
    if cnt == m and number not in book:
        book[number] = 1
        result.append(number)
        return
    if idx >= n:
        if cnt == m and number not in book:
            book[number] = 1
            result.append(number)
        return
    dfs(idx+1, number+str(nums[idx])+" ", cnt+1)
    dfs(idx+1, number, cnt)

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

result = []
book = dict()

dfs(0,"",0)

for num in result:
    print(num)

#처리하는 과정에서 약간 비효율적으로 코드를 작성한 것 같다