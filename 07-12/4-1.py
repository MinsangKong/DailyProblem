#https://www.acmicpc.net/problem/17143
#백준 17143번 낚시왕(구현, BFS)
#import sys
#input = sys.stdin.readline
from collections import deque

def move():
    newsea = [[[] for _ in range(r)] for _ in range(c)]
    for i in range(c):
        for j in range(r):
            if sea[i][j]:
                s, d, z = sea[i][j].pop()
                nx = i + direction[d][0]*s
                ny = j + direction[d][1]*s
                #print(i,j,nx,ny)
                while True:
                    if 0 <= nx < c and 0 <= ny < r:
                        break
                    else:
                        if nx < 0  :
                            nx = abs(nx)
                        elif ny < 0 :
                            ny = abs(ny)
                        elif nx >= c :
                            nx = c-1-(nx-c+1)
                        elif ny >= r :
                            ny = r-1-(ny-r+1)
                        d = rotate(d)
                #print(nx,ny,d)
                if newsea[nx][ny] :
                    if z > newsea[nx][ny][0][2] :
                        newsea[nx][ny].pop()
                        newsea[nx][ny].append([s,d,z])
                else:
                    newsea[nx][ny].append([s,d,z])
                    
    return newsea
                    
def rotate(d):
    if d < 2:
        return (d+1)%2
    else:
        return (d-1)%2 + 2
            
def fishing(idx):
    size = 0
    for i in range(c):
        if sea[i][idx]:
            s, d, z = sea[i][idx].pop()
            size += z
            break
    return size
        

c, r, m = map(int, input().split())

sea = [[[] for _ in range(r)] for _ in range(c)]

for i in range(m):
    x, y, s, d, z = map(int, input().split())
    if d <= 2 :
        sea[x-1][y-1].append([s%(c*2-2),d-1,z]) #속력, 이동방향, 크기
    else:
        sea[x-1][y-1].append([s%(r*2-2),d-1,z]) #속력, 이동방향, 크기
    
direction = [(-1,0),(1,0),(0,1),(0,-1)]

result = 0
for i in range(r):
    result += fishing(i)
    sea = move()
    
print(result)