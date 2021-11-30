#https://www.acmicpc.net/problem/15927
#백준 15927번 회문은 회문아니야!! (투포인터)
#import sys
#input = sys.stdin.readline

def find(s,e):
    if not check(s,e):
        return e-s+1
    elif not check(s+1,e):
        return e-s
    return -1

def check(s,e):
    num = (e-s+1)//2
    for i in range(num):
        if word[i+s] != word[e-i]:
            return False
    return True

word = input().rstrip()
n = len(word)

print(find(0,n-1))
'''
이해를 잘 못해서 엄청 오래 걸렸다.
애초에 처음 check함수에서 True가 나왔다는건 펠린드롬이기 때문에
s~e-1과 s+1~e는 서로 동일할 수 밖에 없었다. 그러므로 s+1~e까지 펠린드롬인지 추가적으로
체크해준다면 펠린드롬일 경우에는 모든 값이 펠린드롬이 되기 때문데 -1을 반환하고
아니라면 s+1~e까지의 길이만큼만 반환해주면 된다.
'''