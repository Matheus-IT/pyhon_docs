l = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# I can do this:
even = list(filter(lambda val: val%2 == 0, l)) # Take each value to the anonymous function
print(even)

# Or I can also do this:
def evens(val):
    if val%2 == 0:
        return True
    else:
        return False

for even in filter(evens, l):
    print(f' {even} ', end='')
