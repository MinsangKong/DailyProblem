#https://www.acmicpc.net/problem/15686
#백준 15686번 치킨 배달 (구현)
#import sys
#ipnut = sys.stdin.readline
#import sys
#input = sys.stdin.readline
from itertools import combinations 

n, m = map(int, input().split())
city = []
chicken = []
home = []
for i in range(n):
    city.append(list(map(int, input().split())))
    
for i in range(n):
    for j in range(n):
        if city[i][j] == 2:
            chicken.append((i,j))
        elif city[i][j] == 1:
            home.append((i,j))
            
result = int(1e9)
for ch in combinations(chicken, m):
    dist = 0
    for i in home:
        dist += min([abs(i[0]-j[0])+abs(i[1]-j[1]) for j in ch])
        if dist >= result:
            break
    result = min(dist,result)
        
print(result)