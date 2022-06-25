# List Comprehention:
# lista = [val for val in sequência]

l = [n for n in range(10)]
print(f'Numbers list: {l}')

evens = [n for n in range(10) if n%2 == 0]
print(f'Evens: {evens}')

squares = [n**2 for n in range(10)]
print(f'Squares: {squares}')
