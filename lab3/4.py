def print_result(foo):
    def decorated():
        print(foo.__name__)
        print(foo())
        if isinstance(foo(),list):
            print('\n'.join(list(map(str,foo()))))
        elif isinstance(foo(),dict):
            print('\n'.join(["{} = {}".format(key, value) for key, value in foo().items()]))

    return decorated()








@print_result
def test_1():
    return 1





@print_result
def test_2():
    return 'iu'





@print_result
def test_3():
    return {'a': 1, 'b': 2}





@print_result
def test_4():
    return [1, 2]