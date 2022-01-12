#https://www.acmicpc.net/problem/2141
#백준 2141번 우체국 (정렬, 그리디)
#import sys
#input = sys.stdin.readline

n = int(input())
cities = []
total = 0

for _ in range(n):
    a,b = map(int,input().split())
    total += b
    cities.append([a,b])
    
sortedCity = sorted(cities, key = lambda x : (x[0]))
limit = total//2+1 if total%2 else total//2
result = 0
cnt = 0

while cnt < limit :
    cnt += sortedCity[result][1]
    result += 1
    
print(sortedCity[result-1][0])