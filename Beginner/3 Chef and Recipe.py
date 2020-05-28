# /usr/bin/python3.6
# source: https://www.codechef.com/problems/CHEFRECP
# author: audhiaprilliant

for _ in range(int(input())):
    numInput = int(input())
    ingredientList = list(map(int,input().strip().split()))
    statOrder = False
    statDuplicate = False
    uniqueValue = {elem:ingredientList.count(elem) for elem in ingredientList}
    if len(set(list(uniqueValue.values()))) == len(list(uniqueValue.values())):
        statDuplicate = True
    
    dictValue = {elem:1 for elem in uniqueValue.keys()}
    for ind in range(len(ingredientList) - 1):
        if (ingredientList[ind] == ingredientList[ind + 1]):
            dictValue[ingredientList[ind]] += 1
        else:
            dictValue[ingredientList[ind]] += 0
    
    if uniqueValue == dictValue:
        statOrder = True
        
    statPrint = 'NO'
    if statOrder and statDuplicate:
        statPrint = 'YES'
    print(statPrint)