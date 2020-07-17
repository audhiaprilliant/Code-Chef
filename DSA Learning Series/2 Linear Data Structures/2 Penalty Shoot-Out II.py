# /usr/bin/python3.6
# source: https://www.codechef.com/LRNDSA02/problems/PSHOT
# author: audhiaprilliant

for _ in range(int(input())):
    numInput = int(input())
    for _ in range(numInput):
        listPenalty = [int(num) for num in str(input()]
        timA = 0
        timB = 0
        iterNum = 0
        for elem in range(len(listPenalty)):
            if elem % 2:
                timA += listPenalty[elem]
            else:
                timB += listPenalty[elem]