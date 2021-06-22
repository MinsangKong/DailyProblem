l=sorted(int(input())for i in range(9))
for i in l:
    for j in l:
        if i+j==sum(l)-100:
            l.remove(i)
            l.remove(j)
            break
for i in l:
    print(i)