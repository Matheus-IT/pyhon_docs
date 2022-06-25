# A técnica closure consiste em retornar uma função que use internamente variáveis
# (ou nomes) da função que a define.


def greater(fixed_val):
    def _greater(val):
        return val > fixed_val
    return _greater


greater_100k = greater(100000)
print(greater_100k(99999))
print(greater_100k(99999 + 2))
