input()
S = input()
print(max(S.count("BR"), S.count("RB")) + 1)
#보고 진짜 소름이 돋았다... 작업횟수가 늘어난다는 것은 R->B거나 B->R이라는 의미인데
#간단하게 요소를 세주는 것으로 원하는 답을 구할 수 있었다,