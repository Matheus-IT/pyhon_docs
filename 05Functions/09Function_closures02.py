def counter():
    c: int = 0

    def _counter():
        nonlocal c
        c += 1
        return c
    return _counter


count = counter()
print(count())
print(count())
print(count())
