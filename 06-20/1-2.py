def GetMaxBlackJackNumbers(N, M, nums):
    sums = set()
    for i in range(N-2):
	    for j in range(i+1, N-1):
		    for k in range(j+1, N):
			    sum = nums[i] + nums[j] + nums[k]
			    if sum <= M:
				    sums.add(sum)
				    break
    return max([*sums])

N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())), reverse=True)
print(GetMaxBlackJackNumbers(N, M, nums))
'''
combintaion 함수를 쓰는 것보다 3중 포문으로 구한 값을 set에 넣고 가장 큰 값을 추출하는
방법이 훨씬 빨랐다. 중복 여부를 무시하는 것이 시간 효율성이 더 좋았다.
'''