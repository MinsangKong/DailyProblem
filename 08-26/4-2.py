def calc(candidates):
    nums_cp = nums[:]
    idx = 0
    for i in range(len(candidates)):
        if candidates[i] <= 2:
            idx = i+1
        elif candidates[i] == 3:
            nums_cp[idx] *= nums[i+1]
        elif candidates[i] == 4:
            nums_cp[idx] //= nums[i+1]
    total = nums_cp[0]
    for i in range(len(candidates)):
        if candidates[i] == 1:
            total += nums_cp[i+1]
        elif candidates[i] == 2:
            total -= nums_cp[i+1]

    return total


def dfs(depth):
    global min_ans, max_ans, candidates
    if depth == len(nums) - 1:
        res = calc(candidates)
        min_ans = min(min_ans, res)
        max_ans = max(max_ans, res)
        return
    for i in range(1, 5):
        if not operators[i-1]:
            continue
        operators[i-1] -= 1
        candidates[depth] = i
        dfs(depth+1)
        candidates[depth] = 0
        operators[i-1] += 1


N = int(input())
nums = list(map(int, input().split()))
operators = list(map(int, input().split()))
candidates = [0 for _ in range(len(nums)-1)]
min_ans = float('inf')
max_ans = -float('inf')
dfs(0)
print(max_ans)
print(min_ans)