#https://www.acmicpc.net/problem/3040
#백준 3040번 백설 공주와 일곱 난쟁이(그리디)
#import sys
#input = sys.stdin.readline

nums = [int(input()) for _ in range(9)]

total = sum(nums)
pos1, pos2 = 0, 0
flag = False
for i in range(8):
    if flag:
        break
    for j in range(i+1,9):
        if total - (nums[i] + nums[j]) == 100:
            flag = True
            pos1 = i
            pos2 = j
            break
            
for k in range(9):
    if k != pos1 and k != pos2:
        print(nums[k]) 