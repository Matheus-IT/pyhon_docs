# Timer Exemple - This guy shows how long will take to execute
# The function decorated

from time import time


def timer(func):
    def wrapper():
        before = time()
        func()
        print(f'Function took {time() - before} seconds.')
    return wrapper


@timer
def run():
    r = [x for x in range(10000000)]


run()
