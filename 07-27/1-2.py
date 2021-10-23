import sys
import bisect

def eat():
    testCase = int(sys.stdin.readline())
    
    for _ in range(testCase):
        M, N = (map(int, sys.stdin.readline().split()))
        listA = list(map(int, sys.stdin.readline().split()))
        listB = list(map(int, sys.stdin.readline().split()))
    
        listB.sort()
    
        result = 0
    
        for i in listA:
            result += bisect.bisect_left(listB,i)
    
        print(result)

eat()