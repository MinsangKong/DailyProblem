#https://www.acmicpc.net/problem/19583
#백준 19583번 싸이버개강총회(리스트 활용)
import sys

s, e, q = input().split()

start = int("".join(s.split(':')))
end = int("".join(e.split(':')))
close = int("".join(q.split(':')))

book = dict()
result = 0
attendants = dict()
for data in sys.stdin.readlines():
    time, name = data.strip().split(' ')
    time = int("".join(time.split(':')))
    if name in attendants:
            continue
    if name in book:
        if book[name] <= start and end <= time <= close:
            attendants[name] = 1
    else:
        book[name] = time
print(len(attendants))
'''
진짜 이상한 문제인 줄 알았지만 sys.stdin.readlines()을 잘 못 이해했다. 
무조건 split를 해야 정상적으로 된다. 그냥 할 경우 아래와 같은 문제가 발생한다.
a = "21:30 malkoring"
print(a[0],a[1])
time, name = a.strip().split(' ')
print(time, name)
2 1
21:30 malkoring
'''