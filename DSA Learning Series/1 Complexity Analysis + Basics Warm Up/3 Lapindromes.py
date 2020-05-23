# /usr/bin/python3.6
# source: https://www.codechef.com/LRNDSA01/problems/LAPIN
# author: audhiaprilliant

def checkString(text):
    midString = len(text) // 2
    if sorted(text[:midString]) == sorted(text[midString:]):
        return('YES')
    else:
        return('NO')

for i in range(int(input())):
    text = list(str(input()))
    mid = len(text) // 2
    if len(text) % 2:
        text = [x for j,x in enumerate(text) if j != mid]
        print(checkString(text))
    # Case
    else:
        print(checkString(text))