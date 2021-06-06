#https://www.acmicpc.net/problem/1543
#백준 1543번 문서 검색(그리디)
#import sys
#input = sys.stdin.readline

word = input().rstrip()
check = input().rstrip()

cnt = 0
i = 0

while i <= len(word)-len(check):
    if word[i:i+len(check)] == check:
        i+=len(check)
        cnt+=1
    else:
        i+=1
        
print(cnt)