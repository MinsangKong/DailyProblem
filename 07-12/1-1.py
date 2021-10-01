#https://www.acmicpc.net/problem/11655
#백준 11655번 ROT13(문자열)
#import sys
#input = sys.stdin.readline
import string

big = list(string.ascii_uppercase)
small = list(string.ascii_lowercase)
word = list(input().rstrip())

for i in range(len(word)):
    if word[i].isalpha():
        if 'a' <= word[i] <= 'z':
            word[i] = small[(small.index(word[i])+13)%26]
        else:
            word[i] = big[(big.index(word[i])+13)%26]
            
print("".join(word))