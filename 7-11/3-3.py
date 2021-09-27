for T in range(int(input())):
    n, m, k = map(int,input().split())
    house = list(map(int,input().split()))
    res = 0
    cur = sum(house[:m])
    if cur < k:
        res+= 1
    if n == m:
        print(res)
        continue
    for i in range(n-1):
        cur+= house[(i+m)%n] - house[i]
        if cur < k:
            res+= 1
    print(res)