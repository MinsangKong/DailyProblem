import sys
n = int(sys.stdin.readline())
ans = []
for i in range(7):
    file = []
    for j in range(n):
        if j&(1<<i):
            file.append('A')
        else:file.append('B')
    if 'A' not in file:
        file[0] = 'A'
    print(''.join(file))