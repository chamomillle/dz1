x = input("введите данные или оставьте поле пустым для завершения: ")
lst = []
while x:
    lst.append(x)
    x = input("Введите данные или оставить поле пустым для завершения: ")
print("Итоговый список:", lst)
