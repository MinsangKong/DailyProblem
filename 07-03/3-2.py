#https://www.acmicpc.net/problem/16194
#백준 16194번 카드 구매하기 2 (DP)
#import sys
#input = sys.stdin.readline

n = int(input())
cards = [0]+list(map(int, input().split()))

for i in range(1,n+1):
    for j in range(i//2,i): 
        cards[i] = min(cards[i], cards[i-j]+cards[j])
        
print(cards[n])
#속도면에서 개선하기 위해서는 불필요한 부분은 생략해야 한다