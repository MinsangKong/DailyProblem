n = int(input())


k = 2
cnt = 1

while True :
    s = (k*(k+1))//2
    if n < s :
        break
    if n%k == s%k :
        cnt += 1
    k += 1
print(cnt)