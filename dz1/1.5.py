x = float(input())
y = float(input())
if x > 0 and y > 0:
    print(" I четверть")
elif x < 0 and y > 0:
    print(" II четверть")
elif x < 0 and y < 0:
    print(" III четверть")
elif x > 0 and y < 0:
    print(" IV четверть")
elif x != 0 and y == 0:
    print(" точка лежит на оси X ")
elif y != 0 and x == 0:
    print(" точка лежит на оси Y ")
else:
    print(" точка лежит в начале координат ")
