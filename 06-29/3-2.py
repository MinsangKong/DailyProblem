#https://www.acmicpc.net/problem/13022
#백준 13022번 늑대와 올바른 단어(문자열)
#import sys
#input = sys.stdin.readline

def checker():
    if counts[0] == counts[1] and counts[1] == counts[2] and counts[2] == counts[3]:
        return True
    else:
        return False

word = input().rstrip()

book = dict()
book['w'] = 0
book['o'] = 1
book['l'] = 2
book['f'] = 3
counts = [0]*4

flag = True
counts[book[word[0]]] = 1

for i in range(1, len(word)):
    diff = book[word[i]]-book[word[i-1]]
    
    if diff == -3:
        if checker():
            counts = [0]*4
            counts[0] = 1
        else:
            flag = False
            break
    else:
        if 0 <= diff <= 1:
            counts[book[word[i]]]+=1
        else:
            flag = False
            break
if not checker() or not flag:
    print(0)
else:
    print(1)
#각 요소들의 숫자를 배열로 만들고 이를 dict로 관리하여 해결하니까 정답처리됐다