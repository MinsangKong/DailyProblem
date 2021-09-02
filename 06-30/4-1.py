#https://www.acmicpc.net/problem/19566
#백준 19566번 수열의 구간 평균(부분합)
#import sys
#input = sys.stdin.readline
from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(int, input().split()))

result = 0
subSum = 0
subList = defaultdict(int)

for i in range(n):
    subSum+=nums[i]
    point = subSum-(i+1)*k #누적합 추출
    result += subList[point] 
    #결과 값이 기존에 존재하는 값이기 위해서는 현재 nums[i]의 값이 k여야 한다.
    subList[point]+=1
    
#print(subList)
print(result+subList[0])#최종 결과의 값이 0인 요소들을 더해줌