#https://www.acmicpc.net/problem/1934
#백준 1934번 최소 공배수 (정수론)
#import sys
#input = sys.stdin.readline
def gcd(a,b):
    while b :
        a, b = b, a%b
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b)

t = int(input())

for _ in range(t):
    a,b = map(int, input().split())
    print(lcm(a,b))