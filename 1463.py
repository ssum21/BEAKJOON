'''Problem
There are three operations that can be used on integer X as follows.

If X is divisible by 3, divide by 3.
If X is divisible by 2, divide by 2.
Subtract 1.
Given an integer N, we try to make it 1 by appropriately using the three operations above. Output the minimum number of times the operation is used.
'''

import sys
sys.setrecursionlimit(10**7)

num = int(sys.stdin.readline())
tot=0

li=[0 for i in range(num+2)]

def Go(n):
    if(n==1):
        return 0
    elif(li[n]!=0):
        return li[n]
    else:
        if(n%6==0):
            li[n]=min(Go(n//3), Go(n//2))+1
        elif(n%3==0):
            li[n]=min(Go(n//3), Go(n-1))+1
        elif(n%2==0):
            li[n]=min(Go(n//2), Go(n-1))+1
        else:
            li[n]=Go(n-1)+1
        return li[n]
            
print(Go(num))
