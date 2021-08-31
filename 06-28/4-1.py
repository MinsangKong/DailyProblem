#https://www.acmicpc.net/problem/10711
#백준 10711번 모래성(구현)
#import sys
#input = sys.stdin.readline

def checker(x,y):
    cnt = 0
    for a,b in direction:
        nx = x+a
        ny = y+b
        if board[nx][ny] == '.':
            cnt+=1
    if cnt >= int(board[x][y]):
        return True
    else:
        return False

direction = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(1,-1),(-1,1),(-1,-1)]

h, w = map(int, input().split())

board = [list(input().rstrip()) for _ in range(h)]
checkList = []

for i in range(h):
    for j in range(w):
        if board[i][j] != '.' and board[i][j] != '9':
            checkList.append([i,j])
                
result = 0

while True:
    temp = []
    for i in range(len(checkList)):
        if checker(checkList[i][0],checkList[i][1]):
            temp.append(i)
    if temp:
        for idx in range(len(temp)-1,-1,-1):
            board[checkList[temp[idx]][0]][checkList[temp[idx]][1]] = '.'
            del checkList[temp[idx]]
        result+=1
    else:
        print(result)
        break
# 최대한 줄였는데도 11%에서 시간초과 발생