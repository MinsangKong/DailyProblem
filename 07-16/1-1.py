#https://www.acmicpc.net/problem/4446
#백준 4446번 ROT13 (문자열)
import sys

def check(alpha):
    if alpha in vowelBig:
        return 2
    if alpha in vowelSmall:
        return 1
    return 0

small = "bkxznhdcwgpvjqtsrlmf"
big = "BKXZNHDCWGPVJQTSRLMF"
vowelBig = 'AIYEOU'
vowelSmall = 'aiyeou'
    
while True:
    try:
        word = list(input().rstrip())
        for i in range(len(word)):
            num = check(word[i])
            if num == 2:
                idx = vowelBig.index(word[i])
                word[i] = vowelBig[(idx+3)%6]
            elif num == 1:
                idx = vowelSmall.index(word[i])
                word[i] = vowelSmall[(idx+3)%6]
            else:
                if word[i] in big:
                    idx = big.index(word[i])
                    word[i] = big[(idx+10)%20]
                elif word[i] in small:
                    idx = small.index(word[i])
                    word[i] = small[(idx+10)%20]

        print(''.join(word))
    except EOFError:
        break
'''
한 번에 입력받을 때 realines로 처리하는 것이 아니라 read().strip()으로 처리해야
\n이 제거 될 수 있다... 한 번에 처리하는 방법을 너무 사용안해봐서 까먹었다...
'''