def fun1():
    a=10
    print(a)
    def fun2():
        b=20
        print(a)
        print(b)
    fun2()
    print(a)
    # print(b)
fun1()