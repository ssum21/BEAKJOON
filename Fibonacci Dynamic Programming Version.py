#top-down_method -> memorization

import sys
sys.setrecursionlimit(10**7) # fix up error_RecursionError: maximum recursion depth exceeded in comparison

num = int(input())

mz = [-1 for i in range(10001)]
mz[0]=0
mz[1]=1

def fib(n):
    if(mz[n]!=-1):
        return mz[n]
    else:
        mz[n]=fib(n-1)+fib(n-2)
        return mz[n]

print(fib(num))