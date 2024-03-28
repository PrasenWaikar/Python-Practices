dictionary={
    'a':2,
    'b':3
}
print(dictionary)
print(dictionary['a'])
print(dictionary['b'])

list=[
{
    'a':2,
    'b':3
},
{
    'abc':[2,3,4],
    'b':3,
    'c':True
}
]
print(list[1])
print(list[1]['abc'][2])

#overwrite
dict1={
    'a':123,
    'a':3
}
print(dict1['a'])
