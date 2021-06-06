from collections import deque

N, K = map(int, input().split())

if N >= K:
    print(N-K)
    print(1)

else:
    visited = [False] * 100001
    ans = 100001
    amount = 0
    q = deque()
    q.append((K, 0))
    while q:
        pos, cnt = q.popleft()
        visited[pos] = True

        if cnt > ans:
            continue

        if pos == N:
            if cnt < ans:
                ans = cnt
                amount = 1
            elif cnt == ans:
                amount += 1
        
        else:
            if not pos % 2 and not visited[pos % 2]:
                q.append((pos // 2, cnt + 1))
            if 0 <= pos - 1 and not visited[pos-1]:
                q.append((pos - 1, cnt + 1))
            if pos + 1 <= 100000 and not visited[pos+1]:
                q.append((pos + 1, cnt + 1))

    print(ans)
    print(amount)