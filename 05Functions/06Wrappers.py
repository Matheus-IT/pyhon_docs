def f1(func):
    def wrapper():
        print('Started')
        func()
        print('Ended')
    return wrapper


def f2():
    print('Hello')


# I can do this:
# f1(f2)()
# Or this:
x = f1(f2)

x()
