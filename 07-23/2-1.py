#https://www.acmicpc.net/problem/15787
#백준 15787번 기차가 어둠을 헤치고 (구현)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())

trains = [[0]*20 for _ in range(n)]
result = dict()

for _ in range(m):
    data = list(map(int, input().split()))
    if data[0] == 1 :
        trains[data[1]-1][data[2]-1] = 1
    elif data[0] == 2 :
        trains[data[1]-1][data[2]-1] = 0
    elif data[0] == 3 :
        trains[data[1]-1].pop()
        trains[data[1]-1].insert(0,0)
    elif data[0] == 4 :
        trains[data[1]-1].pop(0)
        trains[data[1]-1].append(0)
        
for i in range(n):
    result[str(trains[i])] = 1

print(len(result.keys()))