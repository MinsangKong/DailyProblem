#https://www.acmicpc.net/problem/1747
#백준 1747번 소수&팰린드롬 (정수론, 팰린드롬)
#import sys
#input = sys.stdin.readline

def palindrome(num):
    target = str(num)
    length = len(target)
    for i in range(length//2+1):
        if target[i] != target[length-i-1]:
            return False
    return True        

n = int(input())

prime = [1]*1500000
prime[1] = 0 

for i in range(2,int(1500000**0.5)+1):
    if not prime[i] :
        continue
    for j in range(i+i,1500000,i):
        prime[j] = 0
        
for i in range(n,1500000):
    if prime[i]:
        if palindrome(i):
            print(i)
            break