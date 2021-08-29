#https://www.acmicpc.net/problem/1074
#백준 1074번 Z(정수론, 점화식)
#import sys
#input = sys.stdin.readline

def find(n,r,c):
    if n == 1:
        return r*2+c
    else:
        x = r//2**(n-1)
        y = c//2**(n-1)
        nx = r%2**(n-1)
        ny = c%2**(n-1)
        #print(x,y,nx,ny,(x*2+y)*2**n)
        return ((x*2+y)*2**(2*(n-1))+find(n-1,nx,ny))

n, r, c = map(int, input().split())

print(find(n,r,c))