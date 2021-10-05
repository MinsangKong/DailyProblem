#https://www.acmicpc.net/problem/9242
#백준 9242번 폭탄 해제(문자열)
#import sys
#input = sys.stdin.readline
 
result = ""
code = [input() for _ in range(5)]

nums = []
nums.append("**** ** ** ****")
nums.append("  *  *  *  *  *")
nums.append("***  *****  ***")
nums.append("***  ****  ****")
nums.append("* ** ****  *  *")
nums.append("****  ***  ****")
nums.append("****  **** ****")
nums.append("***  *  *  *  *")
nums.append("**** ***** ****")
nums.append("**** ****  ****")

length = len(code[0])
flag = True
for i in code:
    print(*i)
for k in range(0,length,4):
    word = ""
    check = False
    for i in range(5):
        word += code[i][k:k+3]
    for i in range(10):
        if word == nums[i]:
            result += str(i)
            check = True
            break
    if not check:
        print(k)
        flag = False
        break

if flag and int(result)%6 == 0:
    print("BEER!!")
else:
    print("BOOM!!")
'''
아무리 봐도 틀린 이유를 모르겠다. 입력이 너무 이상하게 처리된다... 
이유를 알았다... rstrip()을 하면 마지막 입력을 이상하게 받는다.
정말 최악의 문제다...
'''