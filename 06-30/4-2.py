n,k = map(int,input().split())
l = list(map(lambda x: int(x)-k,input().split()))
psum = l[:]
for i in range(n-1): psum[i+1]=psum[i+1]+psum[i]
dic = {}
ans = 0
for i in psum:
    if i==0: ans+=1
    if i in dic: ans+=dic[i]; dic[i]+=1
    else: dic[i]=1
print(ans)
'''
입력받을 때에도 lambda를 사용하여 처리할 수 있다.
'''