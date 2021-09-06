n=int(input())
L=list(map(int,input().split()))
S=sum(L)
ans=0
for i in L:
    S-=i
    ans += i*S
print(ans)
#훨씬 더 간결한 코드를 통해 누적합으로 구할 수 있었다.