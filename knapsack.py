import django

dic = [{'w':2, 'v':6}, {'w':2, 'v':10}, {'w':3, 'v':12}]
#money = {}
max_wt1 = 5
max_val = 0
def calc(max_wt):
    max_val=0
    if max_wt<=0:
        return 0
    for x in dic:
        temp = 0
        #print("x[w] is:", x['w'])
        if x['w']<=max_wt:
            #print("x[w] is:", x['w'])
            temp = x['v'] + calc(max_wt - x['w'])
            #print("temp value:", temp)
        #print("max value before:",max_val)
        if max_val<temp:
            max_val = temp
        #print("max value after",max_val)
    return  max_val

value = calc(max_wt1)
print("max val",value)
