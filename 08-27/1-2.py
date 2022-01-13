import sys
input = sys.stdin.readline

N = int(input())

def strike_ball(x,y):
    x = str(x)
    y = str(y)
    s=0
    b=0
    for i in range(3):
        if x[i] == y[i]:
            s +=1
        elif x[i] in y:
            b +=1
    return s,b
def dup(x):
    x = str(x)
    if(x[0] == x[1]):
        return True
    elif(x[0] == x[2]):
        return True
    elif(x[1] == x[2]):
        return True
    return False

old = []
for i in range(100,1000):
    if(dup(i) or '0' in str(i)):
        continue
    old.append(i)
    #print(i)

new = []

for h in range(N):
    com = list(map(int,input().split()))
    num = com[0]
    strike = com[1]
    ball =com[2]

    for number in old:
        if(strike_ball(num,number) == (strike,ball)):
            #print(strike_ball(num,number) , strike,ball)
            new.append(number)
    old = new
    new = []

#print(old)
print(len(old))