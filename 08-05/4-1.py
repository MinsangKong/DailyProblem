#https://www.acmicpc.net/problem/21277
#백준 21277번 짠돌이 호석 (구현, 완전탐색)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

def rotate():
    global n1, m1,board1
    temp = [[0]*51 for _ in range(51)]
    
    for i in range(m1-1,-1,-1):
        for j in range(n1):
            temp[m1-1-i][j] = board1[j][i]
            
    board1 = temp[:]        
    n1,m1 = m1,n1
    
def count(x,y):
    for i in range(x,x+n1):
        for j in range(y,y+m1):
            if board[i][j] and board1[i-x][j-y]:
                return INF
    minx = min(x,50)
    miny = min(y,50)
    maxx = max(x+n1-1,49+n2)
    maxy = max(y+m1-1,49+m2)
    return (maxx-minx+1)*(maxy-miny+1)

n1, m1 = map(int, input().split())
board1 = [[0]*51 for _ in range(51)]
for i in range(n1):
    data = input().rstrip()
    for j in range(m1):
        if data[j] == '1':
            board1[i][j] = 1
n2, m2 = map(int, input().split())
board2 = [[0]*51 for _ in range(51)]
for i in range(n2):
    data = input().rstrip()
    for j in range(m2):
        if data[j] == '1':
            board2[i][j] = 1
            
board = [[0]*151 for _ in range(151)] #전체 보드 
result = INF

for i in range(n2):
    for j in range(m2):
        #퍼즐 2는 가운데 고정시켜두기
        #현재 퍼즐의 꼭지점 : (50, 50), (50, 49 + m2), (49 + n2, 50), (49 + n2, 49 + m2) 
        board[i+50][j+50] = board2[i][j]
        
for k in range(4):
    rotate()
    for i in range(100):
        for j in range(100):
            #첫 칸을 기준으로 비교
            result = min(count(i,j),result)
print(result)
'''
https://kau-algorithm.tistory.com/182 참고,
이 문제의 포인트는 모든 경우의 수를 포함하는 배열을 만들어야 한다. 
최대 퍼즐 배열과 전체 액자 배열을 만든 뒤 하나의 퍼즐 배열을 고정하고, 나머지 하나만 계속
회전하는 형태로 구현하면 최대 1억의 연산이 존재하기 때문에 충분히 시간 내에 처리할 수 있다.
'''