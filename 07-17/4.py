#https://www.acmicpc.net/problem/3687
#백준 3687번 성냥개비(DP, 그리디)
#import sys
#input = sys.stdin.readline

def getMax(n):
    result = [1 for _ in range(n//2)]
    if n%2 == 1 :
        result[0] = 7 #성냥개비 3개로 만들 수 있는 숫자는 7
    return result

def getMin(n):
    result = [8 for i in range((n+6)//7)]
    if n%7 == 1 : #8개로 표현할 수 있는 가장 작은 값 10???이 된다
        result[0], result[1] = 1, 0
    elif n%7 == 2 :#2개로 표현할 수 있는 가장 작은 값 1
        result[0] = 1
    elif n%7 == 3 :#17개로 만들 수 있는 값중에 가장 작은 값인 200??이 됨
        result[0], result[1], result[2] = 2, 0, 0
    elif n%7 == 4 : #4개로 만들 수 있는 값은 48???이지만
                    #11개로 만들 수 있는 값중에 가장 작은 값은 20???이 된다
        result[0],result[1] = 2, 0 
    elif n%7 == 5: #5개로 만들 수 있는 값 중에 가장 작은 값 2
        result[0] = 2
    elif n%7 == 6 : #6개로 만들수 있는 값 중에 가장 작은 값 6
        result[0] = 6
    return result

t = int(input())

dp = [0,0,1,7,4,2,6,8,10,18,22]

for _ in range(t):
    n = int(input())
    if n < 11 :
        print(dp[n], end = " ")
    else:
        print(*getMin(n), sep='',end=' ')
    print(*getMax(n), sep='')
'''
숫자 한 개를 표현하는데 사용되는 성냥개비의 개수
2개 : 1, 3개 : 7, 4개 : 4, 5개 : 2,3,5, 6개 : 6,9,0, 7개 : 8
==>
가장 적게 사용해서 표현하는 숫자 : 1 (2개 사용)
가장 많이 사용해서 표현하는 숫자 : 8 (7개 사용)
==>
결과적으로 큰 수는 111..., 7111... 의 형태이고, 작은 수는 ???88888...의 형태를 가짐
'''