#https://www.acmicpc.net/problem/1018
#백준 1018번 체스판 다시 칠하기 (구현)
#import sys
#input = sys.stdin.readline

a, b = map(int,input().split())
board=[input().rstrip() for _ in range(a)]
ans1=[]
ans2=[]
k1=[]
k2=[]
    
for i in range(0,8):
    if i%2==0:
        ans1.append("BWBWBWBW")
        ans2.append("WBWBWBWB")
    else:
        ans1.append("WBWBWBWB")
        ans2.append("BWBWBWBW")
        
for _ in range(0,a-7):
    k1.append([0]*(b-7))
    k2.append([0]*(b-7))
    
for q in range(0,a-7):
    for p in range(0,b-7):
        for i in range(q,q+8):
            for j in range(p,p+8):
                if board[i][j]!=ans1[i-q][j-p]:
                    k1[q][p]+=1
                if board[i][j]!=ans2[i-q][j-p]:
                    k2[q][p]+=1
                    
print(min(min(map(min,k1)),min(map(min,k2))))