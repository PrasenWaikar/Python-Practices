def outer():
    print("inside an outer fun")
    def inner():
        print("inside an inner fun")
    inner()
outer()