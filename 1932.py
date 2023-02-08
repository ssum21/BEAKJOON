h=int(input())

arr = [[0 for j in range(h)] for i in range(h)]
carr = [[0 for j in range(h)] for i in range(h)]

for i in range(h):
    temp=input().split()
    for j in range(i+1):
        arr[i][j]=int(temp[j])

carr[0][0]=arr[0][0]

for i in range(1,h):
    for j in range(i+1):
        if(j==0):
            carr[i][j]=arr[i][j]+carr[i-1][j]
        elif(carr[i-1][j-1]>carr[i-1][j]):
            carr[i][j]=arr[i][j]+carr[i-1][j-1]
        else:
            carr[i][j]=arr[i][j]+carr[i-1][j]

print(max(carr[h-1]))

'''.vscode/
        elif(j==i):
            carr[i][j]=arr[i]+carr[i-1][j-1]
            '''

