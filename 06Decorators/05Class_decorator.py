class TraceCall():
    def __init__(self, f):
        self.f = f

    # Para implementar um decorator usando uma classe, você deve criar uma
    # classe que implementa o método especial __call__():
    def __call__(self, *args, **kwargs):
        print("Function executed: {} args: {}".format(self.f.__name__, args))
        self.f(*args, **kwargs)


@TraceCall
def add(a, b):
    return a + b


add(1, 3)
