from graphics import rectangle
from graphics import circle

l=int(input("Enter Length of Rectangle:"))
b=int(input("Enter Breadth of Rectangle:"))
rectangle.area(l,b)
rectangle.perimeter(l,b)

r=int(input("Enter radius of the circle:"))
circle.area(r)
circle.perimeter(r)