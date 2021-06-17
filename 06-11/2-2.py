def test_solution():
    assert solution(
        10,
        [10, -4, 3, 1, 5, 6, -35, 12, 21, -1],
    ) == 54


def get_dp(n, nums):
    dp = [0] * n
    dp[0] = nums[0]

    for i in range(n):
        dp[i] = nums[i]
        if i == 0:
            continue
        if dp[i] < dp[i - 1] + nums[i]:
            dp[i] = dp[i - 1] + nums[i]
    return dp


def get_dp_r(n, nums):
    dp = [0] * n
    for i in range(n - 1, -1, -1):
        dp[i] = nums[i]
        if i == n - 1:
            continue
        if dp[i] < dp[i + 1] + nums[i]:
            dp[i] = dp[i + 1] + nums[i]
    return dp


def solution(n, nums):
    dp_l = get_dp(n, nums)
    dp_r = get_dp_r(n, nums)

    ans = max(dp_l)
    for i in range(1, n - 1):
        if ans < dp_l[i - 1] + dp_r[i + 1]:
            ans = dp_l[i - 1] + dp_r[i + 1]

    return ans


n = int(input())
nums = list(map(int, input().split()))
print(solution(n, nums))