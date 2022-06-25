# De forma análoga à list comprehensions, a dict comprehension funciona da
# mesma forma, porém o resultado é um dicionário

prod: list = ['teclado', 'mouse', 'monitor', 'cabo HDMI']
val: list = [35, 65, 550.5, 20]
shopping: dict = {k: v for k, v in zip(prod, val) if v > 50}
print(shopping)
