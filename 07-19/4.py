#https://www.acmicpc.net/problem/2900
#백준 2900번 프로그램(누적합, DP)
#import sys
#input = sys.stdin.readline

def count(cnt, jump):
    for i in range(0,n,jump):
        prefix[i] += cnt

n, k = map(int, input().split())
arr = [0]*n

nums = list(map(int, input().split()))
prefix = [0]*n
counter = [0]*n

#0부터 시작하기 때문에 이를 미리 고려해야한다 
prefix[0] = k 
arr[0] = k

for num in nums:
    counter[num] += 1
    
for i in range(n):
    if counter[i] :
        count(counter[i],i)
        
for i in range(1,n):
    arr[i] = arr[i-1]+prefix[i]

q = int(input())

for _ in range(q):
    a,b = map(int, input().split())
    if a == 0 :
        print(arr[b])
    else:
        print(arr[b]-arr[a-1])