from random import randint

comp_number = randint(0, 100)
your_number = int(input())
while comp_number != your_number:
    if comp_number > your_number:
        print("загаданное число больше!")
    else:
        print("загаданное число меньше!")
    your_number = int(input())
print("вы угадали число!")
