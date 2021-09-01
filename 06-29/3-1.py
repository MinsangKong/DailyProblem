#https://www.acmicpc.net/problem/13022
#백준 13022번 늑대와 올바른 단어(문자열)
#import sys
#input = sys.stdin.readline

def checker(b,a):
    if a == 'w' and b == 'o':
        return True
    if a == 'o' and b == 'l':
        return True
    if a == 'l' and b == 'f':
        return True
    return False

word = input().rstrip()

flag = True
startFlag = False
cnt = 1
n = 1

for i in range(1,len(word)):
    if word[i] == word[i-1]:
        cnt+=1
    else:
        if checker(word[i],word[i-1]):
            if not startFlag:
                startFlag = True
                n = cnt
                cnt = 1
            else:
                if n != cnt:
                    flag = False
                    break
                else:
                    cnt = 1
        else:
            if word[i] == 'w' and word[i-1] == 'f' and cnt == n :
                cnt = 1
                n = 1
                startFlag = False
            else:
                flag = False
                break
if flag:
    print(1)
else:
    print(0)
#30% 언저리에서 틀렸습니다가 나온다... 이유를 모르겠다