n = int(input())

d = [0]*(n+1)
d[0:4] = [1, 2, 7, 22]

def dp(n):
    dx = 0
    if n <= 3:
        return d[n]
    
    for i in range(3, n + 1):
        dx += d[i - 3]
        d[i] = (2 * d[i - 1] + 3 * d[i - 2] + 2*dx) % 1000000007

    return d[n]
print(dp(n))