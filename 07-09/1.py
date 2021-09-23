#https://www.acmicpc.net/problem/15721
#백준 15721번 번데기(점화식)
#import sys
#input = sys.stdin.readline

n = int(input())
t = int(input())
state = int(input())

cnt = 8
idx = 1
total = 8

while True:
    if t <= cnt//2:
        break
    t -= cnt//2
    cnt += 2
    idx += 1
    total += cnt
    
total -= cnt
    
last = [0,1,0,1]+[0]*(idx+1)+[1]*(idx+1)
        
for i in range(len(last)):
    if state == last[i]:
        t -= 1
        if t == 0 :
            total += i
            break

print(total%n)