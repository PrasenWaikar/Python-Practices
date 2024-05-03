"""  
    Define a class, which have a class parameter and have a same instance parameter.

"""
class MyClass:
    class_param = "class parameter"

    def __init__(self, instance_param):
        self.instance_param = instance_param

# Example usage
instance = MyClass("instance parameter")
print("Class parameter:", MyClass.class_param)
print("Instance parameter:", instance.instance_param)
