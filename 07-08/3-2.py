#https://www.acmicpc.net/problem/20542
#백준 20542번 받아쓰기(LCS, 문자열)
#import sys
#input = sys.stdin.readline

def check(x,y):
    if x == y or (x == 'i' and y in ['j','l']) or (x == 'v' and y == 'w'):
        return True
    return False

n, m = map(int, input().split())
word = " "+input().rstrip()
answer = " "+input().rstrip()

dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    dp[i][0] = i
for j in range(1, m+1):
    dp[0][j] = j
    
for i in range(1,n+1):
    for j in range(1,m+1):
        if check(word[i],answer[j]):
            dp[i][j] = dp[i-1][j-1]
        else:
            # 추가, 삭제, 수정 중 가장 적은 것
            dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j],dp[i][j-1]))+1
            
print(dp[n][m])
'''
앞의 알고리즘이 시간 초과라면 이해가 갈텐데 왜 틀렸는지 잘 모르겠다.
편집 알고리즘도 알아보니 well-known이었다. 후...
https://hsp1116.tistory.com/41 참고
'''