import sys
input = sys.stdin.readline
point = []
for _ in range(3):
    point.append(list(map(int, input().split())))
    
def ccw(p1, p2, p3):
    return (p1[0]*p2[1] + p2[0]*p3[1] + p3[0]*p1[1]) - (p2[0]*p1[1] + p3[0]*p2[1] + p1[0]*p3[1])

result = ccw(point[0], point[1], point[2])
if result > 0:
    print(1)
elif result == 0:
    print(0)
else:
    print(-1)


'''
I tried to find it using the number of cases without going through the cross product, but failed

import sys
input = sys.stdin.readline
point = []
for _ in range(3):
    point.append(list(map(float, input().split())))

X1=point[0][0]
X2=point[1][0]
X3=point[2][0]
Y1=point[0][1]
Y2=point[1][1]
Y3=point[2][1]

if((X2-X1)==0):
    temp=Y2-Y1
    if(temp>0 and X1<X3):
        print(-1)
    elif(temp>0 and X1>X3):
        print(1)
    elif(temp<0 and X1<X3):
        print(1)
    elif(temp<0 and X1>X3):
        print(-1)
    else:
        print(0)
elif((Y2-Y1)==0):
    temp=X2-X1
    if(temp>0 and Y1<Y3):
        print(1)
    elif(temp>0 and Y1>Y3):
        print(-1)
    elif(temp<0 and Y1<Y3):
        print(-1)
    elif(temp<0 and Y1>Y3):
        print(1)
    else:
        print(0)
else:
    inc=(Y2-Y1)/(X2-X1)
    if(inc>0):
        temp=Y1-(inc*X1)
        if(Y3==(inc*X3+temp)):
            print(0)
        elif(Y3>(inc*X3+temp)):
            print(1)
        else:
            print(-1)
    else:
        temp=Y1-(inc*X1)
        if(Y3==(inc*X3+temp)):
            print(0)
        elif(Y3>(inc*X3+temp)):
            print(-1)
        else:
            print(1)
'''