#https://www.acmicpc.net/problem/2613
#백준 2613번 숫자 구슬 (파라매트릭 서치)
#import sys
#ipnut = sys.stdin.readline

def check(target):
    cnt = 0
    total = 0
    for i in range(n):
        if nums[i] > target :
            return False
        total += nums[i]
        if total > target :
            cnt += 1
            total = nums[i]
        elif total == target:
            cnt += 1
            total = 0
    if total :
        cnt += 1
    return cnt <= m

n, m = map(int, input().split())
nums = list(map(int, input().split()))

s = max(nums)
e = sum(nums)
result = 0

while s < e :
    mid = (s+e) // 2
    if check(mid) :
        e = mid
    else:
        s = mid + 1
        
print(e)
answer = []
cost = 0
cnt = 0

for i in range(n):
    cnt += 1
    cost += nums[i]
    if cost > e :
        answer.append(cnt-1)
        cnt = 1
        cost = nums[i]
    elif cost == e :
        answer.append(cnt)
        cnt = 0
        cost = 0
if cost :
    answer.append(cnt)

sub = m - len(answer)
for i in range(sub):
    for j in range(len(answer)):
        if answer[j] > 1 :
            answer[j] -= 1
            answer.insert(j,1)
            break
            
print(*answer)