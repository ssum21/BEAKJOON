a=1000-int(input())
temp=0
while(a>0):
    if(a>=500):
        a-=500
        temp+=1
    elif(a>=100):
        a-=100
        temp+=1
    elif(a>=50):
        a-=50
        temp+=1
    elif(a>=10):
        a-=10
        temp+=1
    elif(a>=5):
        a-=5
        temp+=1
    else:
        a-=1
        temp+=1

print(temp)