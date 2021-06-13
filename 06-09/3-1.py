#https://www.acmicpc.net/problem/3151
#백준 3151번 합이 0(투포인터, 정렬)
#import sys
#input = sys.stdin.readline

n = int(input())
spec = list(map(int, input().split()))

spec.sort()

minus = []
plus = []

for i in range(n):
    if spec[i] > 0:
        minus.append(spec[i])
    else:
        plus = spec[i:]
        break
        
if len(plus) < 2:
    print(0)
else:
    cnt = 0
    for i in minus:
        left = 0
        right = len(plus)-1
        num = i
        while left < right:
            total = plus[left]+plus[right]+num
            if total >= 0:
                if total == 0:
                    cnt+=1
                    if left+1 != right and plus[left] == plus[left+1]:
                        left +=1
                    else:
                        right -= 1
                else: 
                    right -=1
            else:
                left += 1
    print(cnt)
    
'''
개념을 잘 못 생각했다...
plus와 minus로 나누지 않고 하나를 기준점으로 잡은 다음에 하는 방식으로 풀어야했다
'''