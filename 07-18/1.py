#https://www.acmicpc.net/problem/10988
#백준 10988번 팰린드롬인지 확인하기(문자열)
#import sys
#input = sys.stdin.readline

word = input().rstrip()

s = 0
e = len(word)-1
flag = True

while s < e:
    if word[s] != word[e]:
        flag = False
        break
    s += 1
    e -= 1
    
print(1 if flag else 0)