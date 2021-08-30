import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())
string = list(input().strip())
sol = 0
l = 0
c_dict = defaultdict(int)
for r, c in enumerate(string):
    c_dict[c] += 1
    if len(c_dict.keys()) > N:
        while l < r and len(c_dict.keys()) > N:
            c_dict[string[l]] -= 1
            if c_dict[string[l]] == 0:
                del(c_dict[string[l]])
            l += 1
    sol = max(sol, r - l + 1)
print(sol)