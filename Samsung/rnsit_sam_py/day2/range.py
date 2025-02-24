def my_range(*args):
    if len(args) == 1:
        i = 0
        while i < args[0]:
            yield i
            i += 1
    elif len(args) == 2:
        i = args[0]
        while i < args[1]:
            yield i
            i += 1
    elif len(args) == 3:
        i = args[0]
        if args[0] < args[1] and args[-1] > 0:
            while i < args[1]:
                yield i
                i += args[-1]
        elif args[0] > args[1] and args[2] < 0:
            while i > args[1]:
                yield i
                i += args[2]

for i in my_range(40, 80, 4):
    print(i, end = '  ')