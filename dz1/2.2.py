s = [] #список
a = input("вводите числа по одному и без пробелов (в начале и конце). "
          " чтобы перейти к результату, введите пустую строку: ")
while a != "":
    s.append(a)
    a = input("вводите числа по одному и без пробелов (в начале и конце). "
              "чтобы перейти к результату, введите пустую строку: ")
else:
    s = sorted(s, reverse = True) 
    string = ""
    for m in s:
        string = string + m 
    print(string)