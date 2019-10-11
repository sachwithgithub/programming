list1 = [3,4,1,5,2,8,6,9,12,10,11]

def merge(a,b):
    index1 = 0
    index2 = 0
    list3 = []
    while(index1<=len(a)-1 and index2<=len(b)-1):
        if a[index1]< b[index2]:
            list3.append(a[index1])
            index1+=1
        elif a[index1]> b[index2]:
            list3.append(b[index2])
            index2+=1
        else:
            list3.append(a[index1])
            index1+=1
            index2+=1
    while(index1<=len(a)-1):
        list3.append(a[index1])
        index1 += 1
    while(index2<=len(b)-1):
        list3.append(b[index2])
        index2 += 1
    return list3

def merge_sort(list1):
    print(list1)
    if len(list1)==1:
        return list1
    left = 0
    right = len(list1)-1
    mid = (left+right)//2
    list2 = merge_sort(list1[left:mid+1])
    list3 = merge_sort(list1[mid+1:])
    return merge(list2,list3)

#merge_sort(list1)
print(merge_sort(list1))