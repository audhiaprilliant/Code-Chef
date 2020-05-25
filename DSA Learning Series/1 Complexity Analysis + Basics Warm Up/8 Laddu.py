# /usr/bin/python3.6
# source: https://www.codechef.com/LRNDSA01/problems/LADDU
# author: audhiaprilliant

dictActiv = {'CONTEST_WON':300,'TOP_CONTRIBUTOR':300,'BUG_FOUND':0,'CONTEST_HOSTED':50}
constrainLaddu = {'INDIAN':200,'NON_INDIAN':400}

for _ in range(int(input())):
    listLaddu = {'INDIAN':0,'NON_INDIAN':0}
    [numUser,origin] = list(map(str,input().strip().split()))
    for _ in range(int(numUser)):
        activUserRank = list(map(str,input().strip().split()))
        tempLaddu = 0
        lenList = len(activUserRank)
        if lenList == 1 and (activUserRank[0] in dictActiv.keys()):
            tempLaddu += dictActiv[activUserRank[0]]
        elif lenList > 1 and (activUserRank[0] in dictActiv.keys()):
            if activUserRank[0] == 'CONTEST_WON':
                if int(activUserRank[1]) in range(1,21):
                    tempLaddu += (20 - int(activUserRank[1]) + dictActiv[activUserRank[0]])
                else:
                    tempLaddu += dictActiv[activUserRank[0]]
            else:
                tempLaddu += (int(activUserRank[1]) + dictActiv[activUserRank[0]])
        else:
            continue
        listLaddu[origin] += tempLaddu
    print(listLaddu[origin] // constrainLaddu[origin])