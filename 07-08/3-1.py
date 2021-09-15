#https://www.acmicpc.net/problem/20542
#백준 20542번 받아쓰기(LCS, 문자열)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
word = " "+input().rstrip()
answer = " "+input().rstrip()

dp = [[""]*(m+1) for _ in range(n+1)]

for i in range(1,n+1):
    for j in range(1,m+1):
        if word[i] == answer[j] or (word[i] == 'i' and answer[j] in ['l','j']) or (word[i] == 'v' and answer[j] == 'w'):
            dp[i][j] = dp[i-1][j-1]+word[i]
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1], key=len)
            
lcs = dp[n][m]
cnt = 0
x, y = 0, 0

for i in range(len(lcs)):
    cntX = 0
    cntY = 0
    
    while x < n :
        x += 1
        if word[x] == lcs[i] or (word[x] == 'i' and lcs[i] in ['l','j']) or (word[x] == 'v' and lcs[i] == 'w'):
            break
        cntX +=1
    while y < m :
        y += 1
        if answer[y] == lcs[i]:
            break
        cntY +=1
    #print(cnt,x,y,cntX, cntY)
    cnt += max(cntX, cntY)
    
cnt += max(n-x, m-y)
print(cnt)
#횟수를 세는 방식은 20%에서 틀렸다고 나옴...