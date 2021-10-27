#https://www.acmicpc.net/problem/3343
#백준 3343번 장미 (그리디,정수론)
import sys
#input = sys.stdin.readline

def gcd(x,y):
    while y:
        x, y = y, x%y
    return x

def lcm(x,y):
    result = (x*y)//gcd(x,y)
    return result

def count(target):
    remain = sys.maxsize
    for i in range(1,target//c+2):
        if i*c >= target:
                remain = min(remain,i*d)
        else:
            rr = target-i*c
            total = i*d
            ar = (rr//a)*b if rr%a == 0 else (rr//a+1)*b
            remain = min(remain,total+ar)
    for i in range(1,target//a+2):
        if i*a >= target:
            remain = min(remain,i*b)
        else:
            rr = target-i*a
            total = i*b
            ar = (rr//c)*d if rr%c == 0 else (rr//c+1)*d
            remain = min(remain,total+ar)
    return remain
                
n,a,b,c,d = map(int, input().split())

base = lcm(a,c)
acost = (base//a)*b
ccost = (base//c)*d
s, r = divmod(n,base)
result = s*min(acost,ccost)

if r == 0 :
    print(result)
elif s == 0 :
    res = count(r)
    print(res)
else :
    res = count(r)
    res2 = count(r+base)
    cost = min(acost,ccost)
    print(min(res+result,result-cost+res2))