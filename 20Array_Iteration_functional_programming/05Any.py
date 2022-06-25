"""any take a list as an argument, and return True if any of their arguments evaluate
to True (and False otherwise)"""
nums = [55, 44, 33, 22, 11]
if any([i % 2 == 0 for i in nums]):
    print('At least one is even')
else:
    print('Nobody is even here')
