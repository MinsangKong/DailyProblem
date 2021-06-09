#https://www.acmicpc.net/problem/9007
#백준 9007번 카누 선수(이분탐색, 투포인터)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

t = int(input())

for _ in range(t):
    k, n = map(int, input().split())
    classes = []
    upClass = []
    downClass = []
    
    for _ in range(4):
        data = list(map(int, input().split()))
        classes.append(sorted(data))
        
    for i in range(n):
        for j in range(n):
            upClass.append(classes[0][i]+classes[1][j])
            downClass.append(classes[2][i]+classes[3][j])
            
    downClass.sort()
    result = INF
    sub = INF
    flag = False
    for i in range(n*n):
        if flag :
            break
        left = 0
        end = n*n-1
        
        while left <= end:
            mid = (left+end)//2
            total = upClass[i]+downClass[mid]
            diff = abs(total-k)
            
            if total == k:
                flag = True
                result = total
                break
            elif total < k :
                start = mid+1
            else:
                end = mid-1
                
            if diff < sub:
                result = total
                sub = diff
            elif diff == sub:
                result = min(result,total)
            
    print(result)
    
'''
2개로 나눠서 이분탐색으로 비교하는 방법은 시간초과 발생
'''