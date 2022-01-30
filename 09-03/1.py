#https://www.acmicpc.net/problem/4134
#백준 4134번 다음 소수 (정수론)
#import sys
#input = sys.stdin.readline

def isPrime(num):
    if num == 0 or num == 1 :
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0 :
            return False
    return True

n = int(input())

for _ in range(n):
    num = int(input())
    while True:
        if isPrime(num):
            print(num)
            break
        else:
            num += 1