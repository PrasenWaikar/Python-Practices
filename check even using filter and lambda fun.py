L=[]
i=0
while(i<5):
    data=int(input("enter num"))
    L.insert(i,data)
    i+=1
res=list(filter(lambda num:num%2==0,L))
print(res)
