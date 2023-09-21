x=float(input())
y=float(input())
if x > 0 and y > 0:
    print(" I четверть")
if x < 0 and y > 0:
    print(" II четверть")
if x < 0 and y < 0:
    print(" III четверть")
if x > 0 and y < 0:
    print(" IV четверть")
if x > 0 or x < 0 and y == 0:
    print(" точка лежит на оси X ")
if y > 0 or y < 0 and x == 0:
    print(" точка лежит на оси Y ")
if x == 0 and y == 0:
    print(" точка лежит в начале координат ")
