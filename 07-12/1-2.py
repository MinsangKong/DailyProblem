for i in input():
    if i.isupper():
        t=ord(i)+13
        if t>90:
            t-=26
        print(chr(t),end='')
    elif i.islower():
        t=ord(i)+13
        if t>122:
            t-=26
        print(chr(t),end='')
    else:
        print(i,end='')