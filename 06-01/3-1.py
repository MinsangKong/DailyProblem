#https://www.acmicpc.net/problem/12851
#백준 12851번 숨바꼭질 2(BFS)
#import sys
#input = sys.stdin.readline
from collections import deque
def direction(n):
    return [n+1,n-1,2*n]

def bfs(n,target):
    q = deque()
    q.append(n)
    cnt[n] = 1
    while q:
        now = q.popleft()
        check = direction(now)
        for i in check:
            if 0 <= i <= 100000:
                if times[i] == 0:
                    cnt[i] += cnt[now]
                    times[i] = times[now]+1
                    q.append(i)
                elif times[i] == times[now]+1:
                    cnt[i]+=cnt[now]


n, k = map(int, input().split())
times = [0]*(100001)
cnt = [0]*(100001)

if n >= k:
    print(n-k)
    print(1)
else:
    bfs(n,k)
    print(times[k])
    print(cnt[k])
'''
2개의 배열을 활용하는 것보다 deque에 node와 횟수를 넣는 방식으로 했으면 더 효율적으로
진행할 수 있었다
'''