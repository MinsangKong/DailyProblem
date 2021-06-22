def countBugs(years):
    years = int(years)
    bugs_history = [[1,1+3,1]]

    for _year in range(2,years+1):
        if _year%2 == 0:
            add_bugs = sum([i[-1] for i in bugs_history if (i[1] >= _year)])
            bugs_history.append([_year,_year+4,add_bugs])
        else:
            add_bugs = sum([i[-1] for i in bugs_history if (i[1] >= _year)])
            bugs_history.append([_year,_year+3,add_bugs])
            
    result = sum([i[-1] for i in bugs_history if i[1] > years])
    return result


years = input()
print(countBugs(years))

'''
일일히 별개의 배열을 만들어서 빼지 않아도 미리 제한을 거는 식으로 하면 훨씬
빠르게 문제를 해결할 수 있었다.
'''