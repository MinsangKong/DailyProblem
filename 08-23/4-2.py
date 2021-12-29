#https://www.acmicpc.net/problem/15831
#백준 15831번 준표의 조약돌 (투 포인터)
#import sys
#input = sys.stdin.readline

n,b,w = map(int, input().split())
load = input().rstrip()
count = {'W' : 0, 'B' : 0}
result = 0

s = 0
e = 0
count[load[s]] += 1
while True:
    if count['W'] >= w :
        if count['B'] <= b :
            result = max(result, e-s+1)
        else:
            while count['B'] > b :
                count[load[s]] -= 1
                s += 1
            if count['W'] >= w :
                result = max(result, e-s+1)
    e += 1
    if e == n :
        break
    count[load[e]] += 1
print(result)
#바보처럼 1 0 0 B에선 셀수가 없는데 단순하게 w가 0이면 1로 처리했다가 계속 틀렸다. 