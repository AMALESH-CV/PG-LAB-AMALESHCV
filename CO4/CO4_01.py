class Rectangle:
    def __init__(self):
        self.length=int(input("Enter the Length: "))
        self.breadth=int(input("Enter the Breadth: "))
        self.area=self.length*self.breadth
        self.perimeter=2*(self.length+self.breadth)
    def display(self):
        print("Area of Rectangle: ",self.area)
        print("Perimeter of Rectangle: ",self.perimeter)

print("Details of Rectangle 1")
p1=Rectangle()
p1.display()
print("Details of Rectangle 2")
p2=Rectangle()
p2.display()

if p1.area>p2.area:
    print("Rectangle 1 with Area", p1.area, "has Larger Area")
else:
    print("Rectangle 2 with Area",p2.area,"has Larger Area")
    