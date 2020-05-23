# /usr/bin/python3.6
# source: https://www.codechef.com/problems/COVID19
# author: audhiaprilliant

for i in range(int(input())):
    n = int(input())
    m = list(map(int,input().strip().split()))[:n]
    num = 1
    mid = []
    case = []
    for ind in range(len(m) - 1):
        if abs(m[ind] - m[ind + 1]) > 2:
            mid.append(ind)
    mid = [j + 1 for j in mid]
    # Append the index
    mid.insert(0,0)
    mid.append(len(m))
    for inx in range(len(mid) - 1):
        dist = m[mid[inx]:mid[inx + 1]]
        case.append(len(dist))
print(min(case),max(case))