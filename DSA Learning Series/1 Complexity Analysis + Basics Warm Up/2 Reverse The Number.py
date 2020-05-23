# /usr/bin/python3.6
# source: https://www.codechef.com/LRNDSA01/problems/FLOW007
# author: audhiaprilliant

for _ in range(int(input())):
    numInput = int(input())
    listnum = [elem for elem in str(numInput)]
    listnum.reverse()
    listReverse = ''.join([str(elem) for elem in listnum])
    print(int(listReverse))