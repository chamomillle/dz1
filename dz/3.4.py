from collections import Counter
from qwe import fy


def ff(x):
    print("Элемент | Частота")
    return Counter(x)
     
x = fy(input())
v = ff(x)
print(*[f'{i} | {v[i]}' for i in v] , sep = '\n') 