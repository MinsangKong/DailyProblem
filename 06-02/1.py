#https://www.acmicpc.net/problem/1269
#백준 1269번 대칭 차집합(자료구조)
#import sys
#input = sys.stdin.readline

n, m = map(int, input().split())

arr1 = set(list(map(int, input().split())))
arr2 = set(list(map(int, input().split())))


print(len(arr1-arr2)+len(arr2-arr1))