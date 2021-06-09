text=input() # 평문
co=input() # 암호

text_num=[] # 평문의 숫자(0~25)를 받을 리스트
co_num=[] # 암호의 숫자(1~26)를 받을 리스트
answer=[] # 정답을 받을 리스트

for i in co:        # 암호를 하나씩 아스키코드로 받아 96을 뺀다(a=97이기 때문).
    co_num.append(ord(i)-96)

for i in text:      # 평문을 하나씩 아스키코드로 받아 97을 뺀다. 공백일 경우 공백은 그대로 넣는다.
    if i!=' ':
        text_num.append(ord(i)-97)
    else:
        text_num.append(i)

while len(co_num)<len(text_num): # 암호가 평문보다 짧을 경우, 암호의 길이를 늘린다.
    co_num+=co_num

for i in range(len(text_num)):          # 평문과 암호를 하나씩 대조해서 평문숫자-암호숫자 실행
    if text_num[i]!=' ':                # 그리고 26으로 나눈 나머지를 answer_num으로 지정
        answer_num=(text_num[i]-co_num[i])%26 # (a의 경우 0%26=0, b는 1%26=1...-1의 경우는
        answer.append(chr(answer_num+97))     # -1%26=25 이므로 z가 된다.)
    else:
        answer.append(' ')
print(''.join(answer))      # answer 리스트를 문자열로 조인해서 출력

'''
ord와 chr을 활용하는 방식이 훨씬 효율적이었다.
'''