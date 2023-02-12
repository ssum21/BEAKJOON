'''Problem
Jaewon became the mayor of a city. The city has a large straight river that divides the city into east and west. However, Jae-Won decided to build a bridge after realizing that the citizens were experiencing great inconvenience in crossing the river because there was no bridge. A suitable place to build a bridge around a river is called a site. As a result of close inspection of the river, Jaewon found that there are N sites on the west side of the river and M sites on the east side. (N ≤ M)
Jaewon is trying to connect the western and eastern sites with a bridge. (At this time, only one bridge can be connected to one site.) Jaewon wants to build as many bridges as possible, so he wants to build as many (N) bridges as there are sites in the west. Write a program that counts the number of bridges that can be built if bridges cannot overlap each other.
'''


import math
num=int(input())

for i in range(num):
    j,k=input().split()
    j=int(j)
    k=int(k)

    print(math.comb(k,j))