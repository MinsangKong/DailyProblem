import sys
read = sys.stdin.readline
N, K = map(int, read().split())
arr = list(map(int, read().split()))
cnt = [0] * 100001
start = 0
res = 0

for end in range(N):
    cnt[arr[end]] += 1
    if cnt[arr[end]] > K:
        res = max(res, end - start)
        while cnt[arr[end]] > K:
            cnt[arr[start]] -= 1
            start += 1
res = max(res, end - start + 1)
print(res)
#이런식으로 값을 인덱스로 하고 그 배열 위치에 값을 저장하는 방식이면 좀 더 빠를 수 있었다.