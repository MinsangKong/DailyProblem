#https://www.acmicpc.net/problem/1251
#백준 1251번 단어 나누기 (문자열)
#import sys
#input = sys.stdin.readline


word = input().rstrip()
n = len(word)
result = []

for i in range(n-2):
    pre = word[:i+1][::-1]
    for j in range(i+1,n-1):
        mid = word[i+1:j+1][::-1]
        last = word[j+1:][::-1]
        result.append(pre+mid+last)
        
result.sort()
print(result[0])