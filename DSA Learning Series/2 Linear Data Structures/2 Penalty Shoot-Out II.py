# /usr/bin/python3.6
# source: https://www.codechef.com/LRNDSA02/problems/PSHOT
# author: audhiaprilliant

for _ in range(int(input())):
    numInput = int(input())
    listPenalty = [int(num) for num in str(input())][:2 * numInput]
    timA,timB = 0,0
    shotA,shotB = numInput,numInput
    iterNum = 0
    for elem in range(len(listPenalty)):
        if elem % 2 == 0:
            shotA -= 1
            if listPenalty[elem] == 1:
                timA += 1
        else:
            shotB -= 1
            if listPenalty[elem] == 1:
                timB += 1
        
        diffGoal = timA - timB
        if diffGoal > 0:
            if diffGoal > shotB:
                iterNum = elem + 1
                break
        elif diffGoal < 0:
            if abs(diffGoal) > shotA:
                iterNum = elem + 1
                break
        else:
            if elem == 2 * numInput - 1:
                iterNum = elem + 1
    print(iterNum)