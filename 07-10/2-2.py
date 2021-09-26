N, M = map(int, input().split())

num_list = list(set(input().split()))
num_list.sort(key=lambda x : int(x))
sum_list = [' ' + i for i in num_list]

for _ in range(M-1):
    num_list = [i + j for i in num_list for j in sum_list]
    
print('\n'.join(num_list))