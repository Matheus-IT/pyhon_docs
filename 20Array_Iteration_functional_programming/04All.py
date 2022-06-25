"""all take a list as an argument, and return True if all of their arguments evaluate
to True (and False otherwise)"""
nums = [55, 44, 33, 22, 11]
if all([n > 5 for n in nums]):
    print('All larger than 5')
else:
    print('Someone isn\'t larger than 5')
