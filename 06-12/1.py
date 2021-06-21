#https://www.acmicpc.net/problem/10809
#백준 10809번 알파벳 찾기(그리디)
#import sys
#input = sys.stdin.readline

word = input().rstrip()
result = [-1]*26
for i in range(len(word)):
    num = ord(word[i])-97
    if result[num] == -1:
        result[num] = i
        
print(*result)