#https://www.acmicpc.net/problem/16472
#백준 16472번 고냥이(투포인터)
#import sys
#input = sys.stdin.readline

n = int(input())
word = list(input().rstrip())
length = len(set(word))

if length <= n:
    print(len(word))
else:
    l = 0
    r = 1
    result = 0
    alpha = [word[l]]
    cnt = 1
    while l < r :
        if r >= len(word):
            break
        if word[r] in alpha:
            cnt+=1
            r+=1
        else:
            alpha.append(word[r])
            if len(alpha) > n:
                result = max(result,cnt)
                l +=1
                r = l+1
                alpha = [word[l]]
                cnt = 1
                continue
            else:
                cnt+=1
                r+=1
    print(result)
'''
투 포인터로는 문제 없이 해결했지만 처음봤을 때 투포인터를 떠올리기가 쉽지 않다...
'''