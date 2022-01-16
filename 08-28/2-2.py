##https://www.acmicpc.net/problem/15661
#백준 15661번 링크와 스타트 (완전탐색)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

def dfs(idx,t1,t2):
    if idx == n :
        if len(t1) == 0 or len(t2) == 0 :
            return INF
        return count(t1,t2)
    case1 = dfs(idx+1,t1+[idx],t2)
    case2 = dfs(idx+1,t1,t2+[idx])
    return min(case1,case2)

def count(t1,t2):
    start = 0
    link = 0
    for i in range(len(t1)):
        for j in range(i+1, len(t1)):
            start += status[t1[i]][t1[j]]+status[t1[j]][t1[i]]
    for i in range(len(t2)):
        for j in range(i+1, len(t2)):
            link += status[t2[i]][t2[j]]+status[t2[j]][t2[i]]
    return abs(start-link)
    
n = int(input())
status = [list(map(int, input().split())) for _ in range(n)]

print(dfs(0,[],[]))
#실1이었던 이유는 단순하게 해당 인덱스의 인원을 t1,t2에 넣은 후의 결과를 비교하면
#간단하게 구할 수 있었다... 하나의 배열에 사고가 고정되서 너무 오래걸리고 많이 틀렸다...