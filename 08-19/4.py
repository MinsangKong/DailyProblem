#https://www.acmicpc.net/problem/16637
#백준 16637번 괄호 추가하기 (dfs)
#import sys
#input = sys.stdin.readline

def dfs(idx, total):
    global result
    
    if idx == len(oper):
        result = max(result, int(total))
        return
    left = str(eval(total+oper[idx]+nums[idx+1]))
    dfs(idx+1, left)
    
    if idx+1 < len(oper):
        temp = str(eval(nums[idx+1]+oper[idx+1]+nums[idx+2]))
        right = str(eval(total+oper[idx]+temp))
        dfs(idx+2,right)

n = int(input())
operation = input().rstrip()
nums, oper = [], []
result = float('-inf')

for op in operation:
    if op.isdigit() :
        nums.append(op)
    else:
        oper.append(op)
        
dfs(0, nums[0])
print(result)