num=int(input())
tot=0

while(num>1):
    if(num%2!=0 and num%3!=0):
        num-=1
        tot+=1
    elif(num%3==0):
        tot+=1
        num=num//3
    elif((num-1)%3==0):
        tot+=1
        num=num-1
    elif(num%2==0):
        tot+=1
        num=num//2
    else:
        tot+=1
        num=num-1

print(tot)