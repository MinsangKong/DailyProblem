import sys
input=sys.stdin.readline

def inside(tmp,arr,k,x,y,size):
    # 상하 반전
    if k == 1:
        for i in range(x,x+size):
            for j in range(y,y+size):
                tmp[x+size-1-(i-x)][j]=arr[i][j]
    elif k == 2:
        for j in range(y,y+size):
            for i in range(x,x+size):
                tmp[i][y+size-1-(j-y)]=arr[i][j]
    elif k == 3:
        for i in range(x,x+size):
            for j in range(y,y+size):
                tmp[x+(j-y)][y+size-1-(i-x)]=arr[i][j]
    elif k == 4:
        for i in range(x,x+size):
            for j in range(y,y+size):
                tmp[x+size-1-(j-y)][y+(i-x)]=arr[i][j]

def sub_op(tmp,arr,k,l):
    for x in range(0, 2 ** N, 2 ** l):
        for y in range(0, 2 ** N, 2 ** l):
            inside(tmp, arr, k, x, y, 2 ** l)
    return tmp


def operation(arr,k,l):
    tmp = [[0] * (2 ** N) for _ in range(2 ** N)]
    if k <= 4:   # k = 1, 2, 3, 4
        return sub_op(tmp,arr,k,l)
    else :
        # 먼저 전체에 연산을 진행
        inside(tmp,arr,k-4,0,0,2**N)
        if l == 0: return tmp
        if k<=6:
            return sub_op(arr,tmp,k-4,l)
        else:
            # 7 -> 8, 8 -> 7
            return sub_op(arr, tmp, (15 - k) - 4, l)

N,R=map(int,input().split())
arr=[list(map(int,input().split())) for _ in range(2**N)]
for _ in range(R):
    k,l=map(int,input().split())
    if l == 0 and k<=4:
        continue
    arr=operation(arr,k,l)

for _arr in arr:
    print(*_arr)