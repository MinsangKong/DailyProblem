#https://www.acmicpc.net/problem/2417
#백준 2417번 정수 제곱근 (그리디)
#import sys
#input = sys.stdin.readline

n = int(input())

result = n**0.5

print(int(result) if result%1 == 0 else int(result)+1)