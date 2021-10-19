n,d=map(int,input().split())
print(''.join(map(str,range(1,n+1))).count(str(d)))
#map 내부에서 range를 처리해서 답을 구할수 있었다.