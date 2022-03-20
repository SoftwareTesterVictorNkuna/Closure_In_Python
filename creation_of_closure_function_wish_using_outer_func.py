def outer(func):
    def inner():
        print("Accessing:",func.__name__)

        return func()
    return inner




def sayHello():
    print("Hello!")

wish = outer(sayHello)
# expression to be decorated with prefix @

wish()