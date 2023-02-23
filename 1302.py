num = int(input())
lib=dict()
for i in range(num):
    name=input()
    if name not in lib:
        lib[name]=1
    else:
        lib[name]+=1

max_freq = max(lib.values())
best_seller = []

for i in lib:
    if max_freq==lib[i]:
        best_seller.append(i)

best_seller.sort()
print(best_seller[0])