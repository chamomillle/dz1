x = int(input())
y = int(input())
s = 0
while (x <= y):
    if x % 5 == 0:
        s += x
    x += 1
print(s)
