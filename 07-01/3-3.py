import sys

def check():
    global n, c, items
    for i in range(n):
        if items[i]>c:
            continue
        elif items[i]==c:
            return 1
        for j in range(i+1,len(items)):
            if items[i]+items[j] == c:
                return 1
            elif items[i]+items[j]>c:
                continue
            else:
                for k in range(j+1,len(items)):
                    if items[i]+items[j]+items[k]==c:
                        return 1
                    if items[i]+items[j]+items[k]<c:
                        break
                # if binary_search(j+1,len(items)-1,c-items[i]-items[j])==1:
                #     return 1
    return 0

def binary_search(start,end,num):
    if num < 0:
        return 0
    while start<= end:
        mid = (start+end) //2

        if items[mid] < num:
            start = mid+1
        elif items[mid] == num:
            return 1
        else:
            end = mid-1

    return 0

#물건의 수 n 무게 c
n,c = map(int,sys.stdin.readline().split())

#아이템
items = list(map(int,sys.stdin.readline().split()))

items.sort(reverse=True)

answer = check()
print(answer)