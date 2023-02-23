dic=dict()
for i in range(int(input())):
    temp=int(input())
    if temp not in dic :
        dic[temp]=1
    else:
        dic[temp]+=1

min_li=[]
max_value = max(dic.values())

for i in dic:
    if(dic[i]==max_value):
        min_li.append(i)
    
min_li.sort()

print(min_li[0])
