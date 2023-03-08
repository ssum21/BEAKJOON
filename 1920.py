numA=int(input())
A=set(map(int, input().split()))
numB=int(input())
B=list(map(int, input().split()))


# arr의 각 원소별로 이분탐색
for num in arr:
    print(1) if num in A else print(0)
