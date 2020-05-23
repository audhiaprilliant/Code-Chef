# /usr/bin/python3.6
# source: https://www.codechef.com/LRNDSA01/problems/ZCO14003
# author: audhiaprilliant

inputInt = int(input())
listRevenue = 0
listBudget = []
for _ in range(inputInt):
    budgetCust = int(input())
    listBudget.append(budgetCust)

listBudget = sorted(listBudget,reverse = True)
lenPot = 1

for listBudgets in listBudget:
    if (lenPot * listBudgets) > listRevenue:
        listRevenue = lenPot * listBudgets
    else:
        listRevenue = listRevenue
    lenPot += 1
print(listRevenue)