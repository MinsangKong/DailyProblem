H,N = map(int, input().split())

if H == N:
    print(1)
else:
    mapSize = abs(H-N) + 1 #지도의 크기

    route = []
    for i in range(mapSize):
        temp = [1]
        for j in range(mapSize-1):
            temp.append(0)
        route.append(temp)
    # print(route)
    # route[0][0] = 1 #시작점
    for x in range(1, mapSize):
        for y in range(1, mapSize):
            # print(x,y)
            if x < y:
                break
            route[x][y] = route[x-1][y] + route[x][y-1]
    print(route[-1][-1])