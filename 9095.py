num = int(input())

def sum(i):
    if(i==1):
        return 1
    elif(i==2):
        return 2
    elif(i==3):
        return 4
    else:
        return sum(i-1)+sum(i-2)+sum(i-3)

for i in range(num):
    n=int(input())
    print(sum(n))