from collections import Counter
from py import f

els = f(input())
ans = Counter(els)
print('Элемент | Частота')
print(*[f'{i} | {ans[i]}' for i in ans], sep='\n')