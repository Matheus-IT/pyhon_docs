def fahrenheit(t):
    return (5/9) * (t-32)


temp = [40, 0, 100, 35.2] #List with some temperatures

# Posso fazer desse jeito:
arr = list(map(fahrenheit, temp)) #Take each element in 'temp' to exceculte 'fahrenheit'
print(arr)

# Ou posso fazer desse jeito:
for t in map(fahrenheit, temp):
    print(f' {t:4.2f} ', end='')
