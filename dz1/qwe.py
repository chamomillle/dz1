def fy(x):
    lst = []
    while x:
        lst.append(x)
        x = input()
    return lst

if __name__ == "__main__":
    x = input()
    print(fy(x))