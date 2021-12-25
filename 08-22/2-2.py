N,K = map(int, input().split())
arr = input().split()

if arr.count('1') < K :
    print(-1)
else:
    lion = [i for i, x in enumerate( arr ) if x == '1']
    print(min(lion[K-1+j] - lion[j] + 1 for j in range(len(lion)-K+1)))
#굳이 이분탐색으로 풀 필요 없이 1의 인덱스를 기준으로 배열을 만들고 카운트 하는 방식만으로 가능했다.