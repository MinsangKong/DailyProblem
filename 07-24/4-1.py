#https://www.acmicpc.net/problem/11054
#백준 가장 긴 바이토닉 부분 수열 (이분탐색)
#import sys
#input = sys.stdin.readline
import bisect

def check(idx):
    cnt = 0
    lis = []

    for i in range(idx+1):
        if not lis or lis[-1] < nums[i] :
            lis.append(nums[i])
            cnt += 1
        else:
            lis[bisect.bisect_left(lis,nums[i])] = nums[i]

    lss = []

    for i in range(n-1,idx,-1):
        if not lss or lss[-1] < nums[i]:
            lss.append(nums[i])
            cnt += 1
        else:
            lss[bisect.bisect_left(lss,nums[i])] = nums[i]
    if lis and lss:
        if lis[-1] == lss[-1]:
            return cnt - 1
    return cnt

n = int(input())

nums = list(map(int, input().split()))
result = 0

for i in range(n):
    result = max(result,check(i))

print(result)
'''
방식 자체는 맞았지만 방문한 기록을 메모라이징해서 DP로 하면 훨씬 더 빠르게 처리할 수 있었다.
입력의 수가 적어서 이 방식으도 안전하게 정답처리가 되었지만 입력이 훨씬 더 컸다면 시간초과의
가능성이 있다... DP에서 포인트는 배열을 한번 거꾸로 뒤집은 뒤 위의 과정을 반복하는 것
그 뒤 max함수를 써서 dp[i]+reverseddp[n-i-1]-1 중 최대를 구하면 된다.
'''