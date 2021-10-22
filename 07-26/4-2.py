import sys

#sys.stdin = open("input.txt","rt")

if __name__ == "__main__" :
    N,M = map(int,input().split()) ## 구슬의 개수, 그룹의 수
    a = list(map(int,input().split()))
    ## 각 그룹의 합 중 최댓값이 최소!로 하는 최댓값 출력
    ## 파라메트릭 서치
    start = max(a)
    end = 100*N
    ans = 1000000000

    while start<=end :
        mid = (start+end)//2

        tmp = 0
        cnt = 1
        for i in range (N) :
            tmp += a[i]
            if tmp > mid :
                cnt+=1
                tmp = a[i]
        ## 그룹이 적어도 cnt개 이상은 있어야 한다. (의미)

        if cnt <= M :
            end = mid-1
            ans = min(ans,mid)
        else :
            start = mid+1

    print(ans)

    cnt = 0
    x = 0
    cnt_list = []
    for i in range (N) :
        x += a[i]
        if x > ans :
            cnt_list.append(cnt)
            x = a[i]
            cnt = 0
        cnt+=1
    else :
        cnt_list.append(cnt)

    difference = M-len(cnt_list)

    for i in range (len(cnt_list)) :
        if cnt_list[i] == 1 :
            print(cnt_list[i],end=' ')
        else :
            while (cnt_list[i]>=2 and difference > 0) :
                print("1",end=' ');
                cnt_list[i] -= 1
                difference -= 1
            print(cnt_list[i],end=' ')