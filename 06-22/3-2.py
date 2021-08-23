N = int(input())
a = '47'
ans = ''
while(N>0):
    x,y = divmod(N-1,2)
    ans = a[y] + ans
    N = x
print(ans)
'''
굳이 마지막에서 안구해도 divmod를 사용해서 나머지가 1이면 7인데 약간 비효율적으로 구했다.
'''