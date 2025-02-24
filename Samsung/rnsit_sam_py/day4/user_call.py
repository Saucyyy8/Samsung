def f1():
    print('From f1')

def f2():
    print('From f2')

def f3():
    print('From f3')

function_name = input('Enter function name:')
functions = {
    'f1' : f1,
    'f2' : f2,
    'f3' : f3
}
if function_name in functions:
    functions[function_name]()

exec(function_name + '()')