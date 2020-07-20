# /usr/bin/python3.6
# source: https://www.codechef.com/LRNDSA02/problems/PSHOT
# author: audhiaprilliant

for _ in range(int(input())):
    numInput = int(input())
    listPenalty = [int(num) for num in str(input())][:2 * numInput]
    timA,timB = 0,0
    iterNum = 0
    for elem in range(1,len(listPenalty),2):
        if (timA != ((numInput // 2) + 1)) & (timB != ((numInput // 2) + 1)):
            timA += listPenalty[elem - 1]
            timB += listPenalty[elem]
            iterNum = (elem + 1)
        else:
            break
    print(iterNum)