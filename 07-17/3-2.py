import sys
input = sys.stdin.readline

T = int(input())
for TestCase in range(0,T,1):
    N,M = map(int,input().rstrip('\n').split())
    rowSum , colSum = [0]*N , [0]*N
    for row in range(N):
        colData = list(map(int,input().rstrip('\n').split()))
        for colIndex, colValue in enumerate(colData):
            rowSum[row] += colValue
            colSum[colIndex] += colValue

    def setMinus(v):
        return v-1
    for query in range(M):
        startX,startY,endX,endY,delta = map(int,input().rstrip('\n').split())
        startX,startY,endX,endY = setMinus(startX),setMinus(startY),setMinus(endX),setMinus(endY)
        rowValue = (endY-startY+1)*delta
        for row in range(startX,endX+1,1):
            rowSum[row] += rowValue
        colValue = (endX-startX+1)*delta
        for col in range(startY,endY+1,1):
            colSum[col] += colValue
    print(*rowSum)
    print(*colSum)