# /usr/bin/python3.6
# source: https://www.codechef.com/LRNDSA01/problems/FCTRL
# author: audhiaprilliant

# 1 long
import re
# Factorial function
def factorial(num):
    if num == 1:
        return(num)
    else:
        return(num * factorial(num - 1))

for _ in range(int(input())):
    numInput = int(input())
    resultFactorial = str(factorial(numInput))[::-1]
    pattern = re.compile(r'^[0]+[0]')
    listZero = pattern.findall(resultFactorial)
    strZero = ''.join([str(elem) for elem in listZero])
    print(len(strZero))

# 2 shortcut
def numZero(num):
    conqueror = 5
    zeroCase = 0
    while (num / conqueror >= 1):
        zeroCase += int(num / conqueror)
        conqueror *= 5
    return(zeroCase)

for _ in range(int(input())):
    print(numZero(int(input())))