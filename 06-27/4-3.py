N = int(input())

S = input()

alp = "abcdefghijklmnopqrstuvwxyz"
check = {}

for index in range(len(alp)):
    check[alp[index]] = 0

answer = 0
left, right = 0, 0
cnt = 0
while right <= len(S):


    if cnt > N:
        check[S[left]] -= 1
        if check[S[left]] == 0:
            cnt -= 1
        left += 1
    else:
        if right == len(S):
            break


        if check[S[right]] == 0:
            cnt += 1

        if cnt <= N:
            answer = max(answer, right - left + 1)
            # print(S[left:right + 1], left, right)

        check[S[right]] += 1
        right += 1


print(answer)