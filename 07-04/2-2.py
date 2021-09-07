N , R = map(int,input().split())
arr2 = [0] + sorted(list(map(int,input().split())))
used = [0]*(N+1)
arr=[]
arr3=[]

def f(n,bi,k):
    global N,arr3
    if n==k:
        arr3.append(tuple(arr[:]))
        return
    
    for i in range(bi,N+1):
        if used[i]==0:
            used[i]=1
            arr.append(arr2[i])
            f(n+1,i,k)
            arr.pop()
            used[i]=0
f(0,1,R)
arrf = sorted(list(set(arr3)))
for i in range(len(arrf)):
    print(*arrf[i])
#dfs로 처리할 때 이 사람처럼 append 및 pop하는 방식으로 했으면 속도 및 메모리 면에서
#조금 더 효율적으로 작성했었을 것 같다.