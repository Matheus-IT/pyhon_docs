class Student():
    def __init__(self):
        self._name = 'John'
        self._age = 18
        self._grades = [9.5, 5.75, 10]


s1 = Student()

# Verify if s1 has the attribute 'name':
print(hasattr(s1, 'name'))

# Sets a new attribute 'average':
setattr(s1, "average", sum(s1._grades) / 3)

# Gets the attribute 'average':
print(f'{getattr(s1, "average"):4.2f}')

# Delete the attribute 'age':
delattr(s1, 'age')
