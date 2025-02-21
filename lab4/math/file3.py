from math import pi, tan
sides=int(input("Enter the number of sides: "))
length=float(input("Enter the length of a side: "))
area=(sides*length**2)/(4*tan(pi/sides))
print(area)