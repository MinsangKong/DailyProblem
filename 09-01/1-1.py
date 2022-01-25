#https://www.acmicpc.net/problem/2941
#백준 2941번 크로아티아 알파벳 (문자열)
#import sys
#input = sys.stdin.readline
alp = input()
cro_alp = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
cnt =0
for i in cro_alp:
    if i in alp :
        cnt+=alp.count(i)
        alp = alp.replace(i,"")
for i in range(cnt):
    alp = alp.replace("0","")
result = len(alp)+cnt
print(result)