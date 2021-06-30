#https://www.acmicpc.net/problem/2745
#백준 2745번 진법 변환(dict)
#import sys
#input = sys.stdin.readline
from string import ascii_uppercase

alpha = list(ascii_uppercase)
idx = 10
 
book = dict()

for i in alpha:
    book[i]=idx
    idx+=1
    
n, b = input().split()
result = 0
pos = 0
if int(b) <= 10:
    for i in range(len(n)-1,-1,-1):
        result+= int(n[i])*(int(b)**pos)
        pos+=1
    print(result)
else:
    for i in range(len(n)-1,-1,-1):
        if '0' <= n[i] <= '9':
            result+= int(n[i])*(int(b)**pos)
        else:
            result+= book[n[i]]*(int(b)**pos)
        pos+=1
    print(result)
    
'''
소름 돋게 간단한 방법이 있었다.
'''