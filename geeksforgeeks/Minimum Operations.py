n = int(input())
array = [0] * (n+1)
for j in range(1, n+1):
    if j % 2 == 0:
        array[j] = min(array[j-1]+1, array[j//2]+1)
    else:
        array[j] = array[j-1] + 1
print(array[n])
    