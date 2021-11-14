num = int(input())
lst = list()

cnt = 0
cnt_Str = str(cnt)
while(len(lst) < num):
    if (cnt_Str.count('666')):
        for j in range(1000):
            lst.append(cnt * 1000 + j)
    elif (cnt_Str[-1] == '6'):
        if (cnt_Str.count('66')):
            for j in range(100):
                lst.append(cnt * 1000 + 6 * 100 + j)
        elif (cnt_Str.count('6')):
            for j in range(10):
                lst.append(cnt * 1000 + 66 * 10 + j)
    else:
        lst.append(cnt * 1000 + 666)

    cnt += 1
    cnt_Str = str(cnt)

print(lst[num - 1])