def my_function(*args):
    print(args, end='  ')
    print(type(args), end='  ')
    print(args[0], end='  ')
    print(args[-1])

my_function(10)
my_function(1, 2 ,3)
my_function([1,2,3,5], 4, 5, 8)
my_function()