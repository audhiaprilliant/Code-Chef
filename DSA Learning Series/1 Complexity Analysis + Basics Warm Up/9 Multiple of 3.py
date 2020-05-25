# /usr/bin/python3.6
# source: https://www.codechef.com/LRNDSA01/problems/MULTHREE
# author: audhiaprilliant

# 1
def constructNum(countNum,dNull,dOne):
    listNum = [dNull,dOne]
    while len(listNum) < countNum:
        factorialTen = sum(listNum) % 10
        listNum.append(factorialTen)
    intDone = ''.join([str(elem) for elem in listNum])
    return(int(intDone))

def multipleThree(countNum,dNull,dOne):
    intNum = constructNum(countNum,dNull,dOne)
    sumList = sum(list(map(int, str(intNum))))
    return(sumList)

for _ in range(int(input())):
    [countNum,dNull,dOne] = list(map(int,input().strip().split()))
    checkNum = multipleThree(countNum,dNull,dOne)
    statThree = True
    if checkNum % 3 != 0:
        statThree = False
    print(statThree)

# 2
def constructNum(countNum,dNull,dOne):
    countStat = countNum
    intNum = dNull + dOne
    while countStat > 2:
        intNum += intNum % 10
        countStat -= 1
    return(intNum)

for _ in range(int(input())):
    [countNum,dNull,dOne] = list(map(int,input().strip().split()))
    checkNum = constructNum(countNum,dNull,dOne)
    statThree = 'YES'
    if checkNum % 3 != 0:
        statThree = 'NO'
    print(statThree)