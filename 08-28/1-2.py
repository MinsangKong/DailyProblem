def Numcheck(doublst, k):
    for i in range(5):
        for j in range(5):
            if doublst[i][j] == k:
                doublst[i][j] = -1
                break

def Bingocheck(doublst):
    cnt = 0
    digsum1 = digsum2 = 0
    for i in range(5):
        h_sum = 0
        for j in range(5):
            if i == j: digsum1 += doublst[i][j]
            if i+j == 4: digsum2 += doublst[i][j]
            h_sum += doublst[i][j]
        if h_sum == -5:
            cnt += 1
    
    if digsum1 == -5: cnt += 1
    if digsum2 == -5: cnt += 1

    for i in range(5):
        v_sum = 0
        for j in range(5):
            v_sum += doublst[j][i]
        if v_sum == -5:
            cnt += 1
    
    if cnt >= 3:
        return True

field = [[i for i in list(map(int, input().split()))] for j in range(5)]
referee = []
for i in range(5):
    referee.extend(list(map(int, input().split())))

for res in range(25):
    Numcheck(field, referee[res])
    if Bingocheck(field):
        print(res+1)
        break