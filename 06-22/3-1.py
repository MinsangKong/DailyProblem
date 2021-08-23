#https://www.acmicpc.net/problem/2877
#백준 2877번 4와 7(그리디)
#import sys
#input = sys.stdin.readline

n = int(input())
idx = 1
#1의 자리 2개, 10의 자리 4개, 100의 자리 8개, 1000의 자리 16개
while True:
    if n > 2 **idx:
        n-=2**idx
        idx += 1
    else:
        break
        
result = [4]*idx
check = bin(n-1)[2:]
point = ''
if len(check) < idx:
    for i in range(idx-len(check)):
        point+='0'
check = point+check

for i in range(idx):
    if check[i] == '1':
        result[i] = 7
print(int("".join(map(str, result))))