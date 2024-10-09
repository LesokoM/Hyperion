import math
side1 = int(input("Enter a side: "))
side2 = int(input("Enter a side: "))
side3 = int(input("Enter a side: "))

s = (side1 + side2 + side3)/2
area = math.sqrt((s*(s-side1)*(s-side2)*(s-side3)))

print("The area of a the triangle is: ", round(area))