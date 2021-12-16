#https://www.acmicpc.net/problem/1969
#백준 1969번 DNA (문자열, 그리디)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())
dna = [input().rstrip() for _ in range(n)]
result = ''
cnt = 0

for j in range(m):
    a, t, g, c = 0, 0, 0, 0
    for i in range(n):
        if dna[i][j] == 'A':
            a += 1
        elif dna[i][j] == 'T':
            t += 1
        elif dna[i][j] == 'G':
            g += 1
        else:
            c += 1
    total = a+t+g+c
    if a >= t and a >= g and a >= c :
        result += 'A'
        cnt += total-a
    elif c >= t and c >= g :
        result += 'C'
        cnt += total-c
    elif g >= t :
        result += 'G'
        cnt += total-g
    else:
        result += 'T'
        cnt += total-t
        
print(result)
print(cnt)