list1 = [1, 2, 3, 4, 5, 1, 6]
target = 10

cache = [[-1 for x in range(len(list1))] for x in range(len(list1))]

print(cache )

for i in range(len(cache)-1):
    sum = list1[i]
    for j in range(i+1,len(cache)):
        if cache[i][j]<0:
            sum = sum + list1[j]
            cache[i][j] = sum

print(cache)