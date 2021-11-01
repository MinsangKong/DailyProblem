#https://www.acmicpc.net/problem/16916
#백준 16916번 부분 문자열 (문자열, KMP)
#import sys
#input = sys.stdin.readline

def getPI(pattern):
    j = 0
    for i in range(1, len(pattern)):
        while j > 0 and pattern[i] != pattern[j]:
            j = pi[j-1]
        if pattern[i] == pattern[j]:
            j += 1
            pi[i] = j
            
def kmp(s, pattern):
    getPI(pattern)
    j = 0
    for i in range(len(s)):
        while j > 0 and s[i] != pattern[j]:
            j = pi[j-1]
        if s[i] == pattern[j]:
            if j == len(pattern)-1:
                return True
            else:
                j += 1
    return False

word = input().rstrip()
keyword = input().rstrip()
pi = [0]*(len(keyword))

if kmp(word, keyword):
    print(1)
else:
    print(0)
#https://www.landlordgang.xyz/82 알고리즘 설명
#https://bowbowbow.tistory.com/6 기본적으로 설명이 잘되어있음