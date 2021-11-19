#https://www.acmicpc.net/problem/19539
#백준 19539번 사과 나무 (정수론, 그리디)
#import sys
#input = sys.stdin.readline

n = int(input())
nums = sorted(list(map(int, input().split())))

remain = 0
one = 0 
two = 0

for i in range(n):
    if nums[i]-remain < 0 :
        a,b = divmod(nums[i], 2)
        if one >= b and two >= a :
            one -= b
            two -= a
            remain -= nums[i]
        elif one >= b :
            one -= nums[i]-2*two
            two = 0
            remain -= nums[i]
        else:
            two -= a-1
            remain -= nums[i]-3
    elif (nums[i]-remain)%3 == 0 :
        remain = 0
        one = 0 
        two = 0
    else:
        if (nums[i]-remain)%3 == 1 :
            remain = 2
            two += 1
        else:
            remain = 1
            one += 1
if remain : 
    print("NO")
else:
    print("YES")