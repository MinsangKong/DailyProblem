#https://www.acmicpc.net/problem/5904
#백준 5904번 Moo 게임(점화식)
#import sys
#input = sys.stdin.readline

n = int(input())
sub = 4
total = 3

while n > total:
    total = 2 * total + sub
    sub += 1
    
sub -= 1

while True:
    before = (total-sub)//2
    
    #구간을 나눠서 범위를 구함
    if n <= before:# 중간의 sub 배열 전에 위치
        sub-=1
        total = before
    elif n > sub+before: #중간의 sub 배열 뒤에 위치
        n -= (before+sub)
        sub -= 1
        total = before
    else: #중간의 sub 배열에 위치
        n -= before
        break
        
if n == 1:
    print("m")
else:
    print("o")
