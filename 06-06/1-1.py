#https://www.acmicpc.net/problem/1718
#백준 1718번 암호(그리디)
#import sys
#input = sys.stdin.readline


Info = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
word = input().rstrip()
key = input().rstrip()
turn = 0

result = ""

for i in word:
    if turn == len(key):
        turn = 0
        
    if i not in Info or key[turn] not in Info:
        result+=' '
    else:
        point = Info.index(i)- Info.index(key[turn])
        result+=Info[point-1]
    turn+=1
    
print(result)