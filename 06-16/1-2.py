N = int(input())
t = [1, 2] * (N//2)
if N%2:
    t += [3]
print(*t)