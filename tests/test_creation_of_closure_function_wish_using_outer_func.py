import creation_of_closure_function_wish_using_outer_func

def test_if_creation_of_closure_function_wish_using_outer_func():
    
    @outer
    def to_be_decorated(func):
        pass

    decorated_function = creation_of_closure_function_wish_using_outer_func(to_be_decorated)



