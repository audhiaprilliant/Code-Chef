# /usr/bin/python3.6
# source: https://www.codechef.com/LRNDSA01/problems/CONFLIP
# author: audhiaprilliant

for _ in range(int(input())):
    numInput = int(input())
    for _ in range(numInput):
        listInput2 = list(map(int,input().strip().split()))
        cardBegin = ['H']
        if listInput2[0] == 2:
            cardBegin = ['T']
        cardBeginAll = cardBegin * listInput2[1]
        for i in range(len(cardBeginAll) + 1):
            for j in range(i):
                if cardBeginAll[j] == 'T':
                    cardBeginAll[j] = 'H'
                else:
                    cardBeginAll[j] = 'T'
        numHeadTail = {x : cardBeginAll.count(x) for x in cardBeginAll}
        quesFinal = 0
        if listInput2[2] == 1:
            quesFinal = numHeadTail['H']
        else:
            quesFinal = numHeadTail['T']
        print(quesFinal)