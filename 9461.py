'''
Problem.
As shown in the figure on the right, the triangles are placed in a spiral shape. The first triangle is an equilateral triangle with side length 1. Then continue adding equilateral triangles in the following process. When the length of the longest side of the spiral is k, an equilateral triangle with length k is added to that side.
The wave band sequence P(N) is the length of the side of the equilateral triangle in the helix. The first 10 numbers from P(1) to P(10) are 1, 1, 1, 2, 2, 3, 4, 5, 7, 9.
Given N, write a program to find P(N).
'''

num = int(input())

arr=[0 for i in range(101)]
arr[0]=1
arr[1]=1
arr[2]=1

def Pado(N):
    if(N==0):
        return 1
    elif(N==1):
        return 1
    elif(N==2):
        return 1
    elif(arr[N]!=0):
        return arr[N]
    else:
        arr[N]=Pado(N-2)+Pado(N-3)
        return arr[N]
    

for i in range(num):
    a=int(input())
    print(Pado(a-1))

'''
Ex code//
wh = [0 for i in range(101)]
wh[1] = 1
wh[2] = 1
wh[3] = 1
for i in range(0, 98):
    wh[i + 3] = wh[i] + wh[i + 1]
t = int(input())
for i in range(t):
    n = int(input())
    print(wh[n])
'''