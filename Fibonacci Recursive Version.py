num = int(input())

def pivot(i):
    if(i==0):
        return 0
    elif(i==1):
        return 1
    else:
        return pivot(i-1)+pivot(i-2)

print(pivot(num))
