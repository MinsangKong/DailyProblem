l=[input() for _ in range(int(input()))]
for v in l:
    if v[::-1] in l:
        print(len(v),v[len(v)//2])
        break