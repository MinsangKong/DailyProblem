import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
NMAX = 10000
childl = [-1 for _ in range(NMAX+1)] #노드의 왼쪽 자식
childr = [-1 for _ in range(NMAX+1)] #노드의 오른쪽 자식
parent = [0 for _ in range(NMAX+1)] #노드의 부모
levell = [0 for _ in range(NMAX+1)] #레벨의 가장 왼쪽 열 번호
levelr = [0 for _ in range(NMAX+1)] #레벨의 가장 오른쪽 열 번호
turn = 0    #차례대로 부여될 열 번호

def inorder(idx, level):
    global turn
    #LEFT
    if childl[idx] != -1:
        inorder(childl[idx], level+1)    #왼쪽 자식 방문
    #VISIT
    turn += 1    #열 번호 증가(방문)
    if levell[level] == 0:    #이 레벨에 처음 방문했다면
        levell[level] = levelr[level] = turn    #현 열 번호를 이 레벨의 제일 왼쪽 열 번호로 등록
    else:    #이 레벨에 방문한 적이 있다면
        levelr[level] = turn    #현 열 번호를 이 레벨의 제일 오른쪽 열 번호로 등록
    #RIGHT
    if childr[idx] != -1:
        inorder(childr[idx], level+1)    #오른쪽 자식 방문


def findroot(idx):    #루트 찾기
    if parent[idx] == 0:    #부모가 없는 노드라면
        return idx    #=나는 루트입니다
    else:    #부모가 있는 노드라면
        return findroot(parent[idx])    #부모의 부모의 부모의.. 계속 찾아갑니다


n = int(input())
for _ in range(n):
    a, b, c = map(int, input().split())
    childl[a] = b
    childr[a] = c
    parent[b] = parent[c] = a

inorder(findroot(1), 1)    #1번 노드는 항상 존재하므로 1번 노드 기준으로 루트를 찾고 중위 순회
width = 0
level = 1
for i in range(1, NMAX+1):
    if levelr[i]-levell[i] > width:    #레벨 i의 너비가 여태 찾은 너비보다 크다?
        level = i    #갱신
        width = levelr[i] - levell[i]    

print(level, width+1)