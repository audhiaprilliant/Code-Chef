# /usr/bin/python3.6
# source: https://www.codechef.com/LRNDSA01/problems/CONFLIP
# author: audhiaprilliant

for _ in range(int(input())):
    numInput = int(input())
    for _ in range(numInput):
        [beginStat,numCard,finalStat] = list(map(int,input().strip().split()))
        if numCard % 2:
            if beginStat == 1:
                quesFinal = finalStat + (numCard // 2) - 1
            else:
                quesFinal = numCard - (finalStat + (numCard // 2) - 1)
        else:
            quesFinal = numCard // 2
        print(quesFinal)
