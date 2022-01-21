#https://www.acmicpc.net/problem/2609
#백준 2609번 최대 공약수와 최소 공배수 (정수론)
#import sys
#input = sys.stdin.readline

def gcd(a,b):
    while b :
        a,b = b,a%b
    return a

def lcm(a,b):
    return (a*b)//gcd(a,b)

a,b = map(int, input().split())
print(gcd(a,b))
print(lcm(a,b))