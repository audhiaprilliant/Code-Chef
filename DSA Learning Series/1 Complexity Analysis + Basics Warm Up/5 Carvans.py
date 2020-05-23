# /usr/bin/python3.6
# source: https://www.codechef.com/LRNDSA01/problems/CARVANS
# author: audhiaprilliant

for _ in range(int(input())):
    numInput1 = int(input())
    listInput2 = list(map(int,input().strip().split()))[:numInput1]
    carMaxNum = 1
    carMax = listInput2[0]
    for ind in range(1,len(listInput2) - 1):
        if (carMax - listInput2[ind]) >= 0:
            carMaxNum += 1
            carMax = listInput2[ind]
    print(carMaxNum)