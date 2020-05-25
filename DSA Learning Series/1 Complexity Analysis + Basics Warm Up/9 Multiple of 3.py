# /usr/bin/python3.6
# source: https://www.codechef.com/LRNDSA01/problems/MULTHREE
# author: audhiaprilliant

def sumNum(numInt):
    sumReturn = 0
    for i in range(len(str(numInt))):
        sumReturn += int(str(numInt)[i])
    return(sumReturn)

dictMod = {1:4,2:12,3:18}
for _ in range(int(input())):
    [countNum,dNull,dOne] = list(map(int,input().strip().split()))
    if countNum < 10:
        lenListNum = countNum
    else:
        lenListNum = 20
    
    listNum = [dNull,dOne]
    while len(listNum) < lenListNum:
        factorialTen = sum(listNum) % 10
        listNum.append(factorialTen)
    strNumCorrect = 0
    statWhile = True
    ind = 3
    while statWhile and ind <= countNum:
        if listNum[ind:(ind + 2)] == [0,0]:
            strNumCorrect = sum(listNum[:ind])
            statWhile = False
        elif listNum[ind:(ind + 2)] == [6,2]:
            lenStat = (countNum - (ind + 2))
            if lenStat % 4 != 0:
                strNumCorrect = sum(listNum[:(ind + 2)]) + sumNum(20 * (lenStat // 4)) + dictMod[lenStat % 4]
            else:
                strNumCorrect = sum(listNum[:(ind + 2)]) + sumNum(20 * (lenStat // 4))
            statWhile = False
        else:
            strNumCorrect = sum(listNum[:ind])
        ind += 1
    statThree = 'NO'
    modThree = strNumCorrect % 3
    if modThree == 0:
        statThree = 'YES'
    print(statThree)
