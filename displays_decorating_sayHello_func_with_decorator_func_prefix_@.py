

def outer(func):
    def inner():
        print("Accessing:",func.__name__)

        return func()
    return inner 



@outer
def sayHello():
    return "Hello!"
sayHello()
