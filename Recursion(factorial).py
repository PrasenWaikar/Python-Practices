def facto(n):
    if n==1:
        return n
    else:
        return n * facto(n-1)

n=7
result=facto(n)
print(result)