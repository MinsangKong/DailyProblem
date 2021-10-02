#https://www.acmicpc.net/problem/1342
#백준 1342번 행운의 문자열(문자열, DFS)
#import sys
#input = sys.stdin.readline

def dfs(depth, nword):
    global cnt
    if depth == length:
        if nword not in result:
            cnt += 1
            result[nword] = 1
        return
    for alpha in alphas:
        if counter[alpha] > 0 and nword[depth-1] != alpha:
            counter[alpha] -= 1
            dfs(depth+1, nword+alpha)
            counter[alpha] += 1

word = input().rstrip()
length = len(word)

counter = dict()
result = dict()

cnt = 1

for i in range(1,length):
    if word[i] == word[i-1]:
        cnt -= 1 
        break
        
if cnt :
    result[word] = 1
        
for i in range(length):
    if word[i] in counter:
        counter[word[i]] += 1
    else:
        counter[word[i]] = 1
        
alphas = sorted(counter.keys())

for alpha in alphas:
    counter[alpha] -= 1
    dfs(1,alpha)
    counter[alpha] += 1
    
#print(result)
print(cnt)
#일반적인 백트래킹 방식은 시간초과 발생