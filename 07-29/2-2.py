N, A, B, C, D = map(int, input().split())

if A/C > B/D:
	A, B, C, D = C, D, A, B

import math
print(min(x*B + math.ceil(max(0, (N-x*A)) / C) * D for x in range(C+1)))