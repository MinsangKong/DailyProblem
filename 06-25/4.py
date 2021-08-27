#https://www.acmicpc.net/problem/20543
#백준 20543번 폭탄 던지는 태영이(부분합)
#import sys
#input = sys.stdin.readline

def find_bomb():
    result = [[0]*n for _ in range(n)]
    r = m//2
    start = r
    end = n-r
    for i in range(start,end):
        for j in range(start,end):
            result[i][j] = board[i-r][j-r]
            if i-r-1 >= 0:
                result[i][j] -= board[i-r-1][j-r]
            if j-r-1 >= 0:
                result[i][j] -= board[i-r][j-r-1]
            if i-r-1 >= 0 and j-r-1 >= 0:
                result[i][j] += board[i-r-1][j-r-1]
            if i-m >= 0:
                result[i][j] += result[i-m][j]
            if j-m >= 0:
                result[i][j] += result[i][j-m]
            if i-m >= 0 and j-m >= 0:
                result[i][j] -= result[i-m][j-m]
    return result

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

result = find_bomb()
for i in range(n):
    temp = []
    for j in range(n):
        temp.append(-result[i][j])
    print(*temp)
'''
https://countrysides.tistory.com/54,
https://do-my-best.tistory.com/60 참고해서 작성
생각보다 까다로워 보이는 문제였지만 점화식으로 작성하여 dp로 구현하면 할만한 문제였다
'''