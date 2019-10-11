#ls = [5,2,-3,-12,5,1,3]
#ls = [5,2,-3,-12,13]
ls = [-2, -3, 4, -1, -2, 1, 5, -3, -2, -3, 4, -1, -2, 1, 5, -3, 1000]
sum_final = 0
sum_temp = 0

for x in ls:
    sum_temp += x
    if sum_temp < 0:
        sum_temp = 0
    if sum_final < sum_temp:
        sum_final = sum_temp
print(sum_final)
    