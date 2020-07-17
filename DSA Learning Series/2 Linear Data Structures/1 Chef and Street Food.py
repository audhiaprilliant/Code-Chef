# /usr/bin/python3.6
# source: https://www.codechef.com/LRNDSA02/problems/STFOOD
# author: audhiaprilliant

for _ in range(int(input())):
    numInput = int(input())
    maxProfit = []
    for _ in range(numInput):
        [numStore,numPeople,price] = list(map(int,input().strip().split()))
        profitDaily = (numPeople // (numStore + 1)) * price
        maxProfit.append(profitDaily)
    print(max(maxProfit))