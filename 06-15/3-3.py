import sys
N = int(sys.stdin.readline().rstrip().rstrip())
arr = []
cnt_dict = {}
for _ in range(N):
    tmp_arr = list(map(int, sys.stdin.readline().rstrip().rstrip().split(" ")))
    if tmp_arr[0] not in cnt_dict:
        cnt_dict[tmp_arr[0]] = 1
    else:
        cnt_dict[tmp_arr[0]] += 1
    if tmp_arr[1] not in cnt_dict:
        cnt_dict[tmp_arr[1]] = -1
    else:
        cnt_dict[tmp_arr[1]] += -1
max_val = 0
max_time = 0
cur_val = 0
sorted_times = sorted(cnt_dict.keys())
for time in sorted_times:
    cur_val += cnt_dict[time]
    if cur_val > max_val:
        max_val = cur_val
        max_time = time
max_time_last = max_time
find_ind = sorted_times.index(max_time)
if find_ind+1 <= len(sorted_times):
    for ind in range(find_ind+1, len(sorted_times)):
        if cnt_dict[sorted_times[ind]] != 0:
            max_time_last = sorted_times[ind]
            break
        else:
            max_time_last = sorted_times[ind]
print(max_val)
print(max_time, max_time_last)