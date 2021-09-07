#https://www.acmicpc.net/problem/1032
#백준 1032번 명령 프롬프트(문자열)
#import sys
#input = sys.stdin.readline

n = int(input())

files = [input().rstrip() for _ in range(n)]

keyword = ""
length = len(files[0])

for i in range(length):
    temp = files[0][i]
    for j in range(1,n):
        if temp != files[j][i]:
            temp = "?"
            break
    keyword+=temp
    
print(keyword)