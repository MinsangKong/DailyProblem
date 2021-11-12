#https://www.acmicpc.net/problem/1359
#백준 1359번 복권 (정수론)
#import sys
#input = sys.stdin.readline
def comb(n,r):
    p = 1
    c = 1
    a, b = n, r
    while b :
        c *= a
        p *= b
        a -= 1
        b -= 1
    return c/p
n, m, k = map(int, input().split())

result = 0.0
cases = comb(n,m)

while m >= k :
    if n-m < m-k :
        k +=1
        continue
        
    result += comb(m,k)*comb(n-m,m-k)/cases
    k += 1
print("{0:.16f}".format(result))