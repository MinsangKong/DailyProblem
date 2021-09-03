#https://www.acmicpc.net/problem/18114
#백준 18114번 블랙 프라이데이(자료구조)
#import sys
#input = sys.stdin.readline

n, c = map(int, input().split())
weights = sorted(list(map(int, input().split())))

book = dict()

for weight in weights:
    book[weight] = 1

check = False

if c in book:
    check = True
else:
    for weight in weights:
        if c-weight in book:
            check = True
            break

if check :
    print(1)
else:
    for i in range(n-1):
        for j in range(i+1,n):
            if c-weights[i]-weights[j] in book:
                check = True
                break
                
    if check:
        print(1)
    else:
        print(0)
#모든 경우에 중복을 고려해야 이상이 없었다