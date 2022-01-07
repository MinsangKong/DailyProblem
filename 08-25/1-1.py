#https://www.acmicpc.net/problem/2422
#백준 2422번 한윤정이 이탈리아에 가서 아이스크림을 사먹는데 (완전탐색)
#import sys
#input = sys.stdin.readline

def comb(num):
    return (num*(num-1)*(num-2))//6
        

n, m = map(int, input().split())
total = comb(n)
count = set()

for _ in range(m):
    a,b = map(int, input().split())
    for i in range(1,n+1):
        if i not in [a,b]:
            case = sorted([a,b,i])
            count.add(tuple(case))
            
print(total-len(count))