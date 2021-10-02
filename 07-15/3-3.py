string = input()
len_s = len(string)
di = {}
ans = 0
for i in string:
    if i not in di:
        di[i] = 0
    di[i] += 1

if len(di) == len_s:
    t = 1
    for i in range(1, len_s+1):
        t *= i
    print(t)
    exit()

elif len(di) == len_s - 1:
    t = 1
    for i in range(1, len_s-1):
        t *= i
    print(t * (len_s * (len_s-1) // 2 - len_s + 1))
    exit()


def isluckystring(s):
    s = ''.join(s)
    for i in range(1, len_s):
        if s[i-1] == s[i]:
            return 0
    return 1


def backtracking(s, cnt):

    if cnt == len_s:
        global ans
        ans += 1
        return
    
    last = s[-1]
    for c in di:
        if di[c] > 0 and c != last:
            s.append(c)
            di[c] -= 1
            backtracking(s, cnt+1)
            s.pop()
            di[c] += 1


for i in di:
    di[i] -= 1
    backtracking([i], 1)
    di[i] += 1

print(ans)