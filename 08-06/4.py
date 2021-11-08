#https://www.acmicpc.net/problem/20442
#백준 20442번 ㅋㅋ루ㅋㅋ (투포인터)
#import sys
#input = sys.stdin.readline

word = input().rstrip()
length = len(word)
lsub = []
rsub = []
result = 0
cnt = 0

for alpha in word:
    if alpha == 'K':
        cnt += 1
    else:
        lsub.append(cnt)
        
cnt = 0
for alpha in word[::-1]:
    if alpha == 'K':
        cnt += 1
    else:
        rsub.append(cnt)
        
rsub.reverse()
l, r = 0, len(lsub)-1

while l <= r:
    result = max(result, r-l+1+2*min(lsub[l],rsub[r]))
    if lsub[l] < rsub[r]:
        l += 1
    else:
        r -= 1

print(result)
'''
https://chanu-ps.tistory.com/24 참고,
알고리즘 분류를 봐서 투포인터로 접근했지만 계속 틀렸다...
이 분 풀이를 보니 어느 정도 접근법을 이해할 수 있었다. 
먼저 idx를 기준으로 왼쪽, 오른쪽의 k의 개수를 세준다. 2개의 배열을 기준으로 투포인터를 진행하면
R의 개수는 r-l+1개, K의 개수는 min(lsub[l],rsub[r])*2임을 알 수 있다.
'''