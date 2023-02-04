'''
Problem 1476.
The country where Junkyu lives uses a different method from the year we use. In the country where Junkyu lives, three numbers are used to indicate the year. Each number represents Earth, Sun, and Moon.

If E is the number representing the earth, S is the number representing the sun, and M is the number representing the moon, these three numbers have different ranges. (1 ≤ E ≤ 15, 1 ≤ S ≤ 28, 1 ≤ M ≤ 19)

One year as we know it can be expressed as 1 1 1 in the country where Junkyu lives. As each year passes, all three numbers are incremented by one. If a number is out of range, it becomes 1.

For example, 15 years can be represented as 15 15 15. However, when one year passes and 16 years pass, it becomes 1 16 16, not 16 16 16. The reason is that 1 ≤ E ≤ 15 exceeds the range.

If E, S, and M are given and a year is 1 1 1 in the country where Junkyu lives, write a program to find how many years E S M is in the country where Junkyu lives.

'''

E, S, M=input().split()

E=int(E)
S=int(S)
M=int(M)

listE=[0 for i in range(10000)]
listS=[0 for i in range(10000)]
listM=[0 for i in range(10000)]

for i in range(E, 10000, 15):
    listE[i]=1
    

for i in range(S, 10000, 28):
    listS[i]=1

    
for i in range(M, 10000, 19):
    listM[i]=1

for i in range(10000):
    if(listE[i]==1 and listS[i]==1 and listM[i]==1):
        print(i)
        break

'''
correct answer

E,S,M,cnt =1,1,1,1

i_E , i_S , i_M = map(int,input().split())

while(True):
    if i_E==E and i_S==S and i_M==M :
        break
    E+=1 ; S+=1 ; M+=1; cnt+=1
    if E>=16 : E-=15
    if S>=29 : S-=28
    if M>=20 : M-=19

print(cnt)

'''