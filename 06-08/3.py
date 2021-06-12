#https://www.acmicpc.net/problem/5052
#백준 5052번 전화번호 목록(정렬)
#import sys
#input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    book = [input().rstrip() for _ in range(n)]
    book.sort()
    flag = True
    for i in range(n-1):
        if book[i] in book[i+1][:len(book[i])]:
            flag = False
            break      
    if flag:          
        print("YES")
    else:
        print("NO")