temperature: list = [40, 0, 100, 35.2]

for t in map(lambda temp: (5/9) * (temp-32), temperature): # This is an anonymous function in python!
    print(f' {t:.2f} ', end='')
