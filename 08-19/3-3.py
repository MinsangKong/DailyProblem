input = __import__('sys').stdin.readline
import sys
n = int(input())
l = []
for i in range(n):
    a,b = map(int,input().split())
    l.append((b,a))
l.sort(reverse=True)
last = l[0][0]
for i in l:
    last = min(last,i[0])-i[1]
    if last<0: print(-1); sys.exit()
print(last)
#이 분의 풀이를 보니까 엄청 효율적으로 풀었다.
#끝나는 시간이 가장 큰 문제를 시작으로 end를 갱신해 주면서 요구하는 값을 구했다.