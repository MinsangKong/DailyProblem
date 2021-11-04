#https://www.acmicpc.net/problem/1316
#백준 1316번 그룹 단어 체커 (문자열)
#import sys
#input = sys.stdin.readline

n = int(input())
result = 0

for _ in range(n):
    word = input().rstrip()
    checker = set()
    checker.add(word[0])
    flag = True
    for i in range(1,len(word)):
        if word[i] != word[i-1] and word[i] in checker:
            flag = False
            break
        else:
            checker.add(word[i]) 
    if flag:
        result += 1
print(result)