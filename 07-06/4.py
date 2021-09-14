#https://www.acmicpc.net/problem/20061
#백준 20061번 도노미노도미노 2 (구현)
#import sys
#input = sys.stdin.readline

def move_green(t, y):
    x = 0
    if t == 2:
        for i in range(6):
            if boardGreen[i][y] or boardGreen[i][y+1]:
                break
            x += 1
        x -= 1
        boardGreen[x][y] = 1
        boardGreen[x][y+1] = 1
    else:
        x = 0
        for i in range(6):
            if boardGreen[i][y]:
                break
            x += 1
        x -= 1
        boardGreen[x][y] = 1
        if t == 3:
            boardGreen[x-1][y] = 1 
        
def move_blue(t, x):
    y = 0
    if t == 3:
        for j in range(6):
            if boardBlue[x][j] or boardBlue[x+1][j]:
                break
            y += 1
        y -= 1
        boardBlue[x][y] = 1
        boardBlue[x+1][y] = 1        
    else:
        for j in range(6):
            if boardBlue[x][j] :
                break
            y += 1
        y -= 1
        boardBlue[x][y] = 1
        if t == 2:
            boardBlue[x][y-1] = 1
        
#행이 가득 찼다면 해당하는 줄을 없애고 위에 있는 줄을 당김
def check():
    global answer
    for i in range(2,6):
        total = sum(boardGreen[i])
        if total == 4:
            removeBlock(0, i)
            answer+=1
    
    for j in range(2,6):
        total = 0
        for i in range(4):
            if boardBlue[i][j]:
                total+=1
        if total == 4:
            removeBlock(1, j)
            answer+=1
    
#해당하는 인덱스를 기준으로 위에 있는 요소들을 당김           
def removeBlock(color, idx):
    if color:
        for j in range(idx,-1,-1):
            if j == 0:
                for i in range(4):
                    boardBlue[i][j] = 0
                return
            else:
                for i in range(4):
                    boardBlue[i][j] = boardBlue[i][j-1]
    else:
        for i in range(idx,-1,-1):
            if i == 0:
                for j in range(4):
                    boardGreen[i][j] = 0
                return
            else:
                for j in range(4):
                    boardGreen[i][j] =boardGreen[i-1][j] 

#연한 색깔 영역을 체크 후 블록이 있다면 제일 아래행을 삭제하고 한행씩 내려옴
def check_light():
    for i in range(2):
        for j in range(4):
            if boardGreen[i][j]:
                removeBlock(0, 5)
                break
    for j in range(2):
        for i in range(4):
            if boardBlue[i][j]:
                removeBlock(1, 5)
                break
            
n = int(input())

boardBlue = [[0]*6 for _ in range(4)]
boardGreen = [[0]*4 for _ in range(6)]

answer = 0

for _ in range(n):
    t, x, y = map(int, input().split())
    
    move_green(t, y)
    move_blue(t, x)
    
    check()
    check_light()
    
cnt = 0

for i in range(2, 6):
    cnt += sum(boardGreen[i])
    
for i in range(4):
    cnt += sum(boardBlue[i][2:])
    
print(answer, cnt, sep = "\n")
'''
https://jae-eun-ai.tistory.com/12 참고
'''