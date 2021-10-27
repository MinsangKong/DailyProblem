from math import ceil
from sys import stdin

N, hero_atk = map(int, stdin.readline().split())
req_hp = 1  # req_hp는 항상 1보다 크거나 같다.
max_hp = 1  # max_hp는 항상 req_hp보다 크거나 같다
for i in range(N):
    type_room, atk, health = map(int, stdin.readline().split())
    if type_room == 1:
        # 몬스터가 공격한 횟수 = 용사가 때린 횟수 -1
        req_hp += ceil(health / hero_atk - 1) * atk
    else:
        hero_atk += atk
        # 치료를 받는다면 req_hp가 줄어든다.
        req_hp = max(1, req_hp - health)

    # 매번 최대 체력을 갱신해줘야한다.
    max_hp = max(max_hp, req_hp)
print(max_hp)