#https://www.acmicpc.net/problem/9251
#백준 9251번 LCS(DP)
#import sys
#input = sys.stdin.readline

word1 = list(input().rstrip())
word2 = list(input().rstrip())

dp = [[0]*len(word2) for _ in range(len(word1))]

for i in range(len(word1)):
    for j in range(len(word2)):
        if word1[i] == word2[j]:
            if i == 0 or j == 0:
                dp[i][j]+=1
            else:
                dp[i][j] = max(dp[i][j],dp[i-1][j-1]+1)
        else:
            dp[i][j] = max(dp[i-1][j],dp[i][j-1])
            
print(dp[len(word1)-1][len(word2)-1])