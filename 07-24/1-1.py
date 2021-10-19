#https://www.acmicpc.net/problem/14912
#백준 14912번 숫자 빈도수(문자열)
#import sys
#input = sys.stdin.readline

num, key = input().split()

result = 0

for i in range(1,int(num)+1):
    target = str(i)
    for digit in target:
        if digit == key:
            result += 1
            
print(result)