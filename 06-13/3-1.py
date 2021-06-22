#https://www.acmicpc.net/problem/17291
#백준 17291번 새끼치기(구현)
#import sys
#input = sys.stdin.readline

n = int(input())

result = []
year = 1
result.append([year,0])

while year < n:
    temp = []
    remove = []
    year+=1
    for i in range(len(result)):
        temp.append([year,0])
        result[i][1]+=1
        if result[i][0] % 2 == 1 and result[i][1] == 3:
            remove.append(i)
        elif result[i][0] % 2 == 0 and result[i][1] == 4:
            remove.append(i)
            
    cnt = 0
    for i in remove:
        result.pop(i-cnt)
        cnt+=1
    result+=temp

print(len(result))
print(result)