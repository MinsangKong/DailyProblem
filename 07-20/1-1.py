#https://www.acmicpc.net/problem/9933
#백준 9933번 민균이의 비밀번호(문자열)
#import sys
#input = sys.stdin.readline

n = int(input())

words = []
for i in range(n):
    data = list(input().rstrip())
    if data[::-1] in words:
        print(len(data), data[len(data)//2])
        break
    else:
        if data == data[::-1]:
            print(len(data), data[len(data)//2])
            break
        else:
            words.append(data)