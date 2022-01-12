#https://www.acmicpc.net/problem/15659
#백준 15659번 연산자 끼워 넣기 (3) (백트래킹)
import sys
#input = sys.stdin.readline

def dfs(idx, op):
    global _max,_min
    if idx == n:
        temp = []
        for i in range(n-1):
            if op[i] >= 2 :
                if len(temp) >= 1 :
                    num = temp.pop()
                    result = calc(op[i],num,nums[i+1])
                    temp.append(result)
                else:
                    num = calc(op[i],nums[i],nums[i+1])
                    temp.append(num)
            else:
                if len(temp) >= 1:
                    temp.append(op[i])
                    temp.append(nums[i+1])
                else:
                    temp.append(nums[i])
                    temp.append(op[i])
                    temp.append(nums[i+1])
        total = temp[0]
        for i in range(1,len(temp),2):
            total = calc(temp[i],total,temp[i+1])
        _max = max(_max, total)
        _min = min(_min, total)
        return
    for i in range(4):
        if opers[i] :
            opers[i] -= 1
            op.append(i)
            dfs(idx+1, op)
            opers[i] += 1
            op.pop()
        
            
def calc(idx,a,b):
    if idx == 0 :
        return a+b
    elif idx == 1 :
        return a-b
    elif idx == 2 :
        return a*b
    else:
        return a//b
            
n = int(input())
nums = list(map(int, input().split()))
opers = list(map(int, input().split()))
_max = -sys.maxsize
_min = sys.maxsize
dfs(1,[])

print(_max,_min,sep = '\n')