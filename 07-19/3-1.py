#https://www.acmicpc.net/problem/10597
#백준 10597번 순열장난(DFS)
#import sys
#input = sys.stdin.readline

nums = input().rstrip()

counter = dict()

for i in range(len(nums)):
    if nums[i] in counter:
        counter[nums[i]] += 1
    else:
        counter[nums[i]] = 1
        
result = 50
flag = True
for i in range(1,51):
    if not flag:
        break
    num = str(i)
    for j in num:
        if counter[j] > 0:
            counter[j] -= 1
        else:
            flag = False
            result = i-1
            break
            
permutation = [0]*(result+1)
permutation[0] = 1
temp = ""
for i in range(len(nums)):
    temp += nums[i]
    if not permutation[int(temp)]:
        permutation[int(temp)] += 1
        print(int(temp), end = " ")
        temp = ""

#카운트해서 순열의 마지막을 기준으로 숫자를 찾아가는 방식은 인덱스에러 발생