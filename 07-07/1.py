#https://www.acmicpc.net/problem/1145
#백준 1145번 적어도 대부분의 배수(완전 탐색)
#import sys
#input = sys.stdin.readline

nums = sorted(list(map(int, input().split())))

result = nums[0]*nums[1]*nums[2]

for i in range(4,result+1):
    cnt = 0
    for num in nums:
        if i % num == 0:
            cnt+=1
    if cnt >= 3:
        print(i)
        break