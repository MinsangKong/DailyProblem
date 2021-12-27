n, m, r = map(int, input().split())
arr = []
for i in range(n):
    row = list(map(int, input().split()))
    arr.append(row)

def compute(i, j, r):
    square_level = min(min(i, abs(n-1-i)), min(j, abs(m-1-j)))
    l_a = n-2*square_level
    l_b = m-2*square_level
    max_index = (l_a-1)*2 + (l_b-1)*2 - 1
    if i == square_level:
        index = max_index + 1 - (j - square_level)
        index = 0 if index == max_index+1 else index
    elif j == square_level:
        index = i - square_level
    elif i == n-1-square_level:
        index = l_a-1 + j - square_level
    else:
        index = l_a-1 + l_b-1 + n-1-square_level-i
    index -= r

    index = index % (max_index+1)
    if index <= l_a-1:
        i, j = index, 0
    elif index <= l_a-1 + l_b-1:
        i, j = l_a-1, index-l_a+1
    elif index <= (l_a-1)*2 + l_b-1:
        i, j = l_a-1-(index-(l_a-1)-(l_b-1)), l_b-1
    else:
        i, j = 0, max_index+1-index
    i += square_level
    j += square_level
    return i, j


_arr = [[0 for _ in range(m)] for _ in range(n)]
for i in range(n):
    for j in range(m):
        _i, _j = compute(i, j, r)
        _arr[i][j] = arr[_i][_j]

for i in range(n):
    print(*_arr[i])