list1 = [1,1,1,1,1]
t =3
count =0
def calc(sum1,i):
    global count
    if i==len(list1):
        if sum1==t:
            count+=1

        return
    #for x in list1:
    #    sum2 = +x + calc()
    #sum3=0
    #sum3+=
    calc(sum1 + list1[i],i+1)
    calc(sum1 - list1[i],i+1)

calc(0,0)
print("count",count)