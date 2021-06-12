#https://www.acmicpc.net/problem/17470
#백준 17470번 배열돌리기 5(최적화,효율성)
#import sys
#input = sys.stdin.readline
from collections import deque

def calc(i,check,flag):
    if i == 1:
        check.rotate(2)
    elif i == 2:
        check.reverse()
        check.rotate(2)
    elif i == 3:
        a,b = check.popleft(),check.popleft()
        check.insert(1,a)
        check.insert(3,b)
    elif i == 4:
        a = check.popleft()
        check.rotate(1)
        b = check.pop()
        check.rotate(1)
        check.append(a)
        check.append(b)
    elif flag and i == 5:
        a,b = check.popleft(), check.popleft()
        check.insert(1,a)
        check.insert(3,b)
    elif flag and i == 6:
        a = check.popleft()
        check.rotate(1)
        b = check.pop()
        check.rotate(1)
        check.append(a)
        check.append(b)
        
n,m,r = map(int, input().split())
height = n//2
width = m//2
board = []

for _ in range(n):
    board.append(list(map(int, input().split())))
    
board_divide = dict()

for i in range(4):
    temp = []
    quo = i//2
    mod = i%2
    startX = quo*(n//2)
    startY = mod*(m//2)
    endX = (quo+1)*(n//2)
    endY = (mod+1)*(m//2)
    for x in range(startX,endX):
        tmp = []
        for y in range(startY,endY):
            tmp.append(board[x][y])
        temp.append(tmp)
    board_divide[i+1] = temp
    
oper_cnt = [0 for _ in range(7)]
oper = list(map(int, input().split()))

small_list = deque([1,2,3,4])
mini_rotate = deque([0,1,2,3])

for op in oper:
    calc(op,small_list,True)
    calc(op,mini_rotate,False)
    
position = [[0,0],[0,m//2-1],[n//2-1,0],[n//2-1,m//2-1]]
one, two, three = mini_rotate.popleft(),mini_rotate.popleft(),mini_rotate.popleft()

for i in range(4):
    origin = position[one]
    left_origin = position[two]
    bottom_origin = position[three]
    
    if origin[0] == left_origin[0] and origin[1] == bottom_origin[1]:
        dx = 1
        dy = 1
        if origin[1] > left_origin[1]:
            dy = -1
        if origin[0] > bottom_origin[0]:
            dx = -1
        temp = []
        
        for x in range(abs(bottom_origin[0]-origin[0])+1):
            tmp = []
            for y in range(abs(origin[1]-left_origin[1])+1):
                tmp.append(board_divide[i+1][origin[0]+x*dx][origin[1]+y*dy])
            temp.append(tmp)
        board_divide[i+1] = temp
    else:
        dx = 1
        dy = 1
        if origin[0] > left_origin[0]:
            dy = -1
        if origin[1] > bottom_origin[1]:
            dx = -1
        temp = []

        for x in range(abs(bottom_origin[1]-origin[1])+1):
            tmp = []
            for y in range(abs(left_origin[0]-origin[0])+1):
                tmp.append(board_divide[i+1][origin[0]+dy*y][origin[1]+dx*x])
            temp.append(tmp)
        board_divide[i+1] = temp
        
lastN = len(board_divide[1])*2
lastM = len(board_divide[1][0])*2

result = [[0 for _ in range(lastM)] for _ in range(lastN)]

for i in range(4):
    idx = small_list.popleft()
    quo = i//2
    mod = i%2
    startX = quo*(lastN//2)
    startY = mod*(lastM//2)
    arr = board_divide[idx]
    for x in range(lastN//2):
        for y in range(lastM//2):
            result[startX+x][startY+y] = arr[x][y]
            
for i in result:
    print(*i)
    
'''
https://welog.tistory.com/313 해설 참고 
이해가 잘 안간다...
'''