def outer(func):
    """
    THis function  implement the creation of decorator ..
     function outer(),which is used to decorate function
     sayHello().
    """

    def inner():
        print('Accessing:',func.__name__)

        return func()
    return inner


def sayHello():
    print("Hello!")

wish=outer(sayHello) 

wish()

    