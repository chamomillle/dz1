from collections import Counter
from qwe import fy


def fre(a):
    return Counter(a)

a = fy()
a = fre(a)
print("Элемент | Частота")
for i in a:
    print(f'{i} | {a[i]}')