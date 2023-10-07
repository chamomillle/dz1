a = input()
k = 0
m = int(input())
for i in a:
    if i.isdigit():
        k += 1
        if k == m:
            print(f'{m}-ая цифра в строке {i}')
    
    