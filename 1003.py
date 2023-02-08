import sys
sys.setrecursionlimit(10**7)

num=int(input())
arr=[0 for i in range(1002)]


def fibonacci(N):
    if (N==0):
        return 0
    elif (N==1):
        return 1
    elif (arr[N]==0 or arr[N]==None):
        arr[N]=fibonacci(N-1)+fibonacci(N-2)
        return arr[N]
    else:
        return arr[N]


print(fibonacci(num+1)%10007)
