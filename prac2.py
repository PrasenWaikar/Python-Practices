def missing(nums):
    a=sorted(nums)
    for i in range(len(a)):
        if a[i]!= i + 1:
            print("missing number is : ",i+1)
            break

nums=[1,2,3,9,5]
missing(nums)