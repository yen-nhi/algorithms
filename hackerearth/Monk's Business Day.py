#Bellman Ford algorithms
#with deals are edges  

def max_profit(n, deals):
    profit = [float("-inf")] * (n+1)
    profit[1] = 0
    for k in range(n-1):
        for (i, j, c) in deals:
            if profit[j] < profit[i] + c:
                profit[j] = profit[i] + c
    for (i, j, c) in deals:
        if profit[j] < profit[i] + c:
            return "Yes"
    return "No"

test = int(input())
for t in range(test):
    n, m = map(int, input().split())
    deals = []
    for u in range(m):
        (i, j, c) = map(int, input().split())
        deals.append((i, j, c))
    print(max_profit(n, deals))

