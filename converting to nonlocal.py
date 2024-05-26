def fun1():
    a=10
    print(a)
    def fun2():
        nonlocal a
        global b
        a=100
        b=200
        print(a)
        print(b)
    fun2()
    print(a)
    print(b)
fun1()