#https://www.acmicpc.net/problem/13902
#백준 13902번 개업 2 (DP)
#import sys
#input = sys.stdin.readline
INF = int(1e9)

n, m = map(int, input().split())
nums = sorted(list(map(int, input().split())))

woks = set()
for i in range(m):
    woks.add(nums[i])
    for j in range(i+1,m):
        if nums[i]+nums[j] > n:
            break
        woks.add(nums[i]+nums[j])
woks = sorted(list(woks))
counts = dict()
for wok in woks:
    counts[wok] = 1
    
if m == 1:
    print(-1 if n%nums[0] else n//nums[0])
else:
    while True:
        temp = dict()
        if len(counts) == 0 or n in counts:
            break
        for count in counts:
            for wok in woks:
                if count+wok > n :
                    continue
                if count+wok in temp :
                    temp[count+wok] = min(temp[count+wok], counts[count]+1)
                else:
                    temp[count+wok] = counts[count]+1
        counts = temp
    print(counts[n] if n in counts else -1)
#계속 갱신해주는 것보다 최대 배열을 만들고 거기서 반복 처리를 하는 것이 더 빨랐다.