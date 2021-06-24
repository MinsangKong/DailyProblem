#https://www.acmicpc.net/problem/4836
#백준 4836번 춤(구현)
import sys

for temp in sys.stdin.readlines():

    dip_checker = True
    dip_index = []
    twirl_flg = False
    hop_flg = False
    dip_flg = False

    target = temp.rstrip().split()

    for i, value in enumerate(target):
        if value == 'dip':
            dip_flg = True

            if i > 0 and target[i-1] == 'jiggle':
                continue
            if i > 1 and target[i-2] == 'jiggle':
                continue
            if i < len(target) - 1 and target[i+1] == 'twirl':
                continue
            dip_checker = False
            dip_index.append(i)

        elif value == 'twirl':
            twirl_flg = True
        elif value == 'hop':
            hop_flg = True

    errors = []
    if dip_flg and not dip_checker:
        errors.append('1')

        dip_temp = []
        start = 0
        for i in dip_index:
            dip_temp.extend(target[start:i])
            dip_temp.append('DIP')
            start = i + 1

        dip_temp.extend(target[start:])
        target = dip_temp

    if target[-3:] != ['clap', 'stomp', 'clap']:
        errors.append('2')

    if twirl_flg and not hop_flg:
        errors.append('3')

    if target[0] == 'jiggle':
        errors.append('4')

    if not dip_flg:
        errors.append('5')


    #　결과 
    result_str = 'form '
    error_len = len(errors)

    if error_len == 0:
        result_str += 'ok: '
        
    else:
        if error_len == 1:
            result_str += 'error '
            result_str += errors[0]
            
        else:
            result_str += 'errors '
            if error_len == 2:
                result_str += ' and '.join(errors)
                
            else:
                result_str += (', '.join(errors[:-1]) + ' and ' + errors[-1])
        result_str += ': '
    print(result_str + ' '.join(target))