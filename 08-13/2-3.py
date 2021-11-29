import sys
input = sys.stdin.readline

def find(s,e):
    if not check(s,e):
        return e-s+1
    
    l = s+1
    r = e
    length = 0
    while l < r :
        if word[l] != word[r]:
            length = max(length, r-l+1)
            break
        l += 1
    l = s
    r = e-1
    while l < r:
        if word[l] != word[r]:
            length = max(length, r-l+1)
            break
        r -= 1
    return length

def check(s,e):
    num = (e-s+1)//2
    for i in range(num):
        if word[i+s] != word[e-i]:
            return False
    return True

word = input().rstrip()
n = len(word)

result = find(0,n-1)

if result :
    print(result)
else:
    print(-1)