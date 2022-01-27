#https://www.acmicpc.net/problem/3613
#백준 3613번 Java vs C++ (문자열)
#import sys
#input = sys.stdin.readline

def toJava(word):
    if word[0] == '_' or word[-1] == '_' or '__' in word:
        return "Error!"
    result = ""
    flag = False
    
    for key in word:
        if key.isupper():
            return "Error!"
        
        if key == "_":
            flag = True
            continue
        
        if flag :
            result += key.upper()
            flag = False
            continue
            
        result += key
    
    return result

def toCpp(word):
    if word[0].isupper() :
        return "Error!"
    result = ""
    
    for key in word:
        if key.isupper():
            result += '_'+key.lower()
            continue
        result += key
        
    return result

word = input().rstrip()

if "_" in word:
    print(toJava(word))
else:
    print(toCpp(word))