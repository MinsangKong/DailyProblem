#https://www.acmicpc.net/problem/14725
#백준 14725번 개미굴(DFS,dict)
#import sys
#input = sys.stdin.readline
def find(tree,key,bar):
    child = tree.get(key)
    if child:
        for i in sorted(child.keys()):
            print(bar+i)
            if child.get(i):
                find(child,i,bar+'--')

n = int(input())
tree = dict()

for _ in range(n):
    data = list(input().split())
    k, info = int(data[0]), data[1:]
    
    if not info[0] in tree:
        tree[info[0]] = dict()
        
    temp = tree
    
    for i in range(1,len(info)):
        children = temp.get(info[i-1])
        if children and (info[i] in children):
            temp = children
            continue
        children[info[i]] = dict()
        temp = children
        
for key in sorted(tree.keys()):
    print(key)
    find(tree,key,'--')