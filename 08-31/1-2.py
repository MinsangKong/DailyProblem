def cheak_number(n):
    a = 1
    b = 2
    if n ==1:
        return 1
    
    while True:
        first = int(n*b/(a+b))
        second = int(n*(a/b))
        
        start = max(first,second)
        last = min(first,second)
        
        
        if n==2 or n==4:
            last=last-1
        
        for i in range(start,last,-1):
            pass
        a,b= b,a+b
        if start<=last+1:
            return i
            break
            
def cal(num1,num2):
    number=[num1,num2]
    while True:
        result=num1-num2      
        if result<0:
            break
        number.append(result)
        num1,num2=num2,result
    print(len(number))
    for i in number:
        print(i, end=" ")

num1= int(input())
num2=cheak_number(num1)
cal(num1,num2)