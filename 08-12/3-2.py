M=[[]for _ in [0]*26]
for _ in[0]*int(input()):
    v,w=input().split(' is ')
    M[ord(v)-97]+=[ord(w)-97]
for _ in[0]*int(input()):
    a,b=input().split(' is ')
    q,v,B=M[ord(a)-97],[],False
    while q and not B:
        q2=[]
        for i in q:
            for j in M[i]:
                if j==ord(b)-97:
                    B=True
                    break
                if j not in v:
                    v+=[j]
                    q2+=[j]
        q=q2
    print(str(B)[0])