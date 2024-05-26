def chekeven(num):
    if(num%2==0):
        return True
    else:
        return False
L=[]
i=0
while(i<5):
    data=int(input("enter num"))
    L.insert(i,data)
    i+=1
res=list(filter(chekeven,L))
print(res)
