input = __import__('sys').stdin.readline
MIS = lambda: map(int,input().split())

def prefsuf(L):
    pref = [0]*n; pref[0] = L[0]
    if pref[0] == 0: pref[0] = 10**9
    for i in range(1, n):
        if L[i] == 0: pref[i] = pref[i-1]
        else: pref[i] = min(pref[i-1], L[i])
    suf = [0]*n; suf[-1] = L[-1]
    for i in range(n-2, -1, -1): suf[i] = max(suf[i+1], L[i])
    return pref, suf

n = int(input())
hap = []
tire = []
for i in range(n):
    x, y = MIS()
    hap.append(x)
    tire.append(y)

prehap, sufhap = prefsuf(hap) # prefix min, suffix max
suftir, pretir = prefsuf(tire[::-1]) # prefix max, suffix min
suftir.reverse()
pretir.reverse()
for i in range(n-2, -1, -1):
    if prehap[i] > sufhap[i+1] and pretir[i] < suftir[i+1]:
        print(i+1); break
else: print(-1)
    
'''
prefix 방식으로 더 쉽게 풀수 있었다...
'''