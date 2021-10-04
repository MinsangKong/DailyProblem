import sys
input = sys.stdin.readline

def checkcheck(r, c, count):
    global paper_count, failed
    if count >= paper_count:
        return
    
    if r == 10:
        if count < paper_count:
            paper_count = count
        return
    if c == 0:
        col_check = 0
        for i in range(10):
            if board[r][i]:
                col_check |= 1<<i
        
        if str(papers) in dp[r][col_check]:
            if dp[r][col_check][str(papers)] > count:
                dp[r][col_check][str(papers)] = count
            else:
                return
        else:
            dp[r][col_check][str(papers)] = count
            
    elif c == 10:
        checkcheck(r+1, 0, count)
        return
    
    marked = is_marked(r,c)
    if marked:
        for i in range(1, marked+1):
            if papers[i-1]>0:
                mark(r,c,i,0)
                papers[i-1]-=1
                checkcheck(r,c+i,count+1)
                mark(r,c,i,1)
                papers[i-1]+=1
            else:
                failed = True
    else:
        checkcheck(r,c+1,count)
    return


def is_marked(r,c):
    if board[r][c]:
        if r < 6 and c < 6:
            if sum([sum(board[r+i][c:c+5]) for i in range(5)]) == 25:
                return 5
        if r < 7 and c < 7:
            if sum([sum(board[r+i][c:c+4]) for i in range(4)]) == 16:
                return 4
        if r < 8 and c < 8:
            if sum([sum(board[r+i][c:c+3]) for i in range(3)]) == 9:
                return 3
        if r < 9 and c < 9:
            if sum([sum(board[r+i][c:c+2]) for i in range(2)]) == 4:
                return 2
        return 1
    else:
        return 0

def mark(r,c,size, flag):
    for dr in range(size):
        for dc in range(size):
            board[r+dr][c+dc] = flag

board = [list(map(int,input().split())) for _ in range(10)]
papers = [5,5,5,5,5]
dp = [[{} for _ in range(1024)] for _ in range(10)]
paper_count = 30
failed = False
checkcheck(0,0,0)
if paper_count == 30:
    paper_count = 0
if not paper_count and failed:
    print(-1)
else:
    print(paper_count)
'''
여기서 규칙을 찾고 dp로 푸는 사람이 있다니...
미쳐버렸다...
'''