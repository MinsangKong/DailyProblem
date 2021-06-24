from collections import deque
class Node:
    def __init__(self,num, level, parent):
        self.num = num
        self.level = level
        self.children = []
        self.findCount = 0
        self.parent = parent
        self.i = -1
        self.j = -1
    
root = Node(1, 0, None)
n = int(input())
binary = input()
x, y = map(int, input().split())
root.i = 1
root.j = len(binary)

current_node = root
current_index = 1
for i, num in enumerate(map(int, binary)):
    if num == 0:
        current_index += 1
        newNode = Node(current_index,current_node.level+1, current_node)
        newNode.i = i+1
        current_node.children.append(newNode)
        current_node = newNode
        if i+1 == x or i+1 == y:
            current_node.findCount += 1
    else:
        current_node.j = i+1
        if i+1 == x or i+1 == y:
            current_node.findCount += 1
        current_node.parent.findCount += current_node.findCount
        current_node = current_node.parent

current_node = root
q = deque()
q.append(current_node)
answer_node = current_node
max_count = 0
while len(q) > 0:
    qsize = len(q)
    for i in range(qsize):
        current_node = q.popleft()
        if current_node.findCount >= max_count:
            answer_node = current_node
            max_count = current_node.findCount
        for c in current_node.children:
            q.append(c)

print(str(answer_node.i) + ' ' + str(answer_node.j))