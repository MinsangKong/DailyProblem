N,M=map(int,input().split())
nums=[]
nums=list(map(int,input().split()))

nums=sorted(nums,reverse=True)
result=0
left=1
right=len(nums)-1
stat=0

for i in range(len(nums)-2):
    left=i+1  
    right=len(nums)-1
    while left<right:
        total=nums[i]+nums[left]+nums[right]
        if total<M:
            result=max(result,total)
            right-=1
        elif total>M:
            left+=1
        else:
            result=M
            stat=1
            break  
    if stat:
        break
print(result)  
'''
이분 탐색을 활용한 방법
'''