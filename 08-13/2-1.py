#https://www.acmicpc.net/problem/16139
#백준 16139번 인간-컴퓨터 상호작용 (누적합)
#import sys
#input = sys.stdin.readline

word = input().rstrip()
q = int(input())
alpha = [[0]*26 for _ in range(len(word)+1)]

for i in range(1,len(word)+1):
    for j in range(26):
        alpha[i][j] = alpha[i-1][j]
    target = ord(word[i-1])-ord('a')
    alpha[i][target] += 1
    
for _ in range(q):
    key, s, e = input().split()
    key = ord(key)-ord('a')
    print(alpha[int(e)+1][key]-alpha[int(s)][key])