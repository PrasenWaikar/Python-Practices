def comm(list1, list2):
    common_elements=[]
    for i in list1:
        if i in list2:
            common_elements.append(i)
    return common_elements
            

list1=[1,2,3,4,5,6,7,8,9]
list2=[9,8,7,6,7,85,6,3,23,12,67,9,0,32]
result=comm(list1, list2)
print(result)