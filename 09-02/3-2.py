def prime(n):
    if n % 2 == 0 and n != 2 or n == 1:
        return 0
    for i in range(3,n//2+1,2):
        if n % i == 0:
            return 0
    return 1

n = int(input())
while True:
    m = str(n)
    if m[::-1] == m:
        if prime(n) == 1:
            break
    n += 1
print(m)