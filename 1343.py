''' Problem
민식이는 다음과 같은 폴리오미노 2개를 무한개만큼 가지고 있다. AAAA와 BB

이제 '.'와 'X'로 이루어진 보드판이 주어졌을 때, 민식이는 겹침없이 'X'를 모두 폴리오미노로 덮으려고 한다. 이때, '.'는 폴리오미노로 덮으면 안 된다.

폴리오미노로 모두 덮은 보드판을 출력하는 프로그램을 작성하시오.

반복문으로 풀려다가 실패함

'''

a=input()
totX=0
temp=True
li=[]
for i in range(len(a)):
    j=i
    i=a[i]
    if(i=='.' and totX%2!=0):
        print('-1')
        temp=False
        break
    elif(i=='.' or j==len(a)):
        if(totX==2):
            li.append('BB')
        totX=0
    elif(i=='X' and totX>=4):
        li.append('AAAA')
        totX=0
    else:
        totX+=1

if(temp):
    print(li)

'''
board = input()

board = board.replace("XXXX", "AAAA")
board = board.replace("XX", "BB")

if 'X' in board:
    print(-1)
    
else:
    print(board)
'''