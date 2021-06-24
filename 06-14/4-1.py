#https://www.acmicpc.net/problem/2233
#백준 2233번 사과나무(트리)
#import sys
#input = sys.stdin.readline

n = int(input())
binary = input()
x,y = map(int, input().split(" "))

def solution(n, binary, x,y):
	def find_parent(current):
		if current == 1:
			return 1
		s1, e1 = dic[current]

		temp_s1, temp_e1 = dic[arr[s1-1]]
		if temp_s1 < s1 and e1 < temp_e1: #서로 부모관계가 형성되려면 먼저 시작하고
			return arr[s1-1]             #자식 node들이 return된 후에 return되야 한다.
		else:
			return arr[e1+1]

	def find_remove_node(current, target):
		s1, e1 = dic[current]
		s2, e2 = dic[target]
		if(s1<=s2 and e2<=e1):
			return current
		return find_remove_node(find_parent(current), target)

	arr = [] 
	stack = [] #방문 기록
	dic = [[0,0] for _ in range(1+n)] # start, end
	x,y = x-1, y-1
	current = 1 
	idx = 0
	answer = 0 # 답은 해당 사과의 +1씩
	for b in binary:
		if b =='0':
			stack.append(current)
			arr.append(current)
			dic[current][0]=idx #현재 node의 부모node 기록
			current+=1

		else:
			temp = stack.pop() 
			arr.append(temp)
			dic[temp][1]=idx #현재 node의 return되는 시점 기록
		idx+=1
	
	first_removable_node = find_remove_node(arr[x], arr[y])
	second_removable_node = find_remove_node(arr[y], arr[x])
	
	s1, e1 = dic[first_removable_node]
	s2, e2 = dic[second_removable_node]

	if e1-s1 <= e2-s1:
		return '%d %d' %   (s1+1, e1+1)
	else:
		return '%d %d' %   (s2+1, e2+1)


print(solution(n,binary,x,y))

'''
https://dlwnsdud205.tistory.com/4
https://m.blog.naver.com/PostView.naver?isHttpsRedirect=true&blogId=p_bysu&logNo=221168531552
참고
'''