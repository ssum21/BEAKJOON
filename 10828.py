import sys
a = int(sys.stdin.readline())

temp=-1
b=[]
t=[]
tot=[]

for i in range(a):
    t = sys.stdin.readline().split()
    b=t[0]
    if(b=='push'):
        c=t[1]
        tot.append(c)
        temp+=1
    elif(b=='pop'):
        if(temp==-1):
            print(-1)
        else:
            print(tot.pop())
            temp-=1
    elif(b=='size'):
        print(temp+1)
    elif(b=='empty'):
        if(temp==-1):
            print(1)
        else:
            print(0)
    else:
        if(temp==-1):
            print(-1)
        else:
            print(tot[temp])

'''
# 문제풀이 방법

파이썬은 따로 stack 구조를 제공하지 않는다.
기본 클래스 list를 이용하여 stack을 표현할 수 있다.

이때, input() 함수를 사용할 경우, 시간초과 에러가 뜨므로 시간단축을 위해 sys.stdin.readline()을 사용한다.
입출력 속도 비교 : sys.stdin.readline > raw_input() > input()

#sys.stdin.readline을 공부하기 위해선 https://velog.io/@yeseolee/Python-%ED%8C%8C%EC%9D%B4%EC%8D%AC-%EC%9E%85%EB%A0%A5-%EC%A0%95%EB%A6%ACsys.stdin.readline 참고

import sys
n = int(sys.stdin.readline())

stack=[]
for i in range(n):
    command = sys.stdin.readline().split()

    if command[0]=='push':
        stack.append(command[1])
    elif command[0]=='pop':
        if len(stack)==0:
            print(-1)
        else:
            print(stack.pop())
    elif command[0] == 'size':
        print(len(stack))
    elif command[0] == 'empty':
        if len(stack)==0:
            print(1)
        else:
            print(0)
    elif command[0] == 'top':
        if len(stack)==0:
            print(-1)
        else:
            print(stack[-1])
'''