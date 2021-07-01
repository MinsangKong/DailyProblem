#https://www.acmicpc.net/problem/10971
#백준 10971번 외판원 순회2(DP,비트마스킹)
import sys
#input = sys.stdin.readline

def find(now, before): 
    # 남아있는 경로를 이미 방문한 적이 있음 
    if dp[now][before]: 
        return dp[now][before] 
    # 모두 방문한 경우 
    if before == (1<<n) - 1: 
        return path[now][0] if path[now][0] > 0 else sys.maxsize 
    # 현재 지점에서 이동할 수 있는 지점들을 탐색 
    cost = sys.maxsize 
    for i in range(1, n):
        if not (before>>i)%2 and path[now][i]: 
            # i부터 0까지 순회를 만든 최소 비용 
            tmp = find(i, before|(1<<i))# before | (1<<i) == before + (1<<i) 
            # (now~i), (i~0)의 합과 현재까지의 최소 비용과 비교 
            cost = min(cost, tmp + path[now][i]) 
            
    # 메모이제이션 
    dp[now][before] = cost 
    return cost 
n = int(input()) 
path = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*(1<<n) for _ in range(n)] 

print(find(0, 1))
'''
시간 제한을 극도로 줄이기 위해선 dp+비트마스킹을 활용하여 문제를 풀어야 한다.
https://suri78.tistory.com/152 참고
https://shoark7.github.io/programming/algorithm/introduction-to-tsp-and-solve-with-exhasutive-search TSP 알고리즘 설명
'''