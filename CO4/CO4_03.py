class rectangle:
    def __init__(self,length,width):
        self.__length=length
        self.__width=width
    def __lt__(self,a1):
        area1=self.__length*self.__width
        area2=a1.__length*a1.__width
        if(area1<area2):
            return(True)
        else:
            return(False)
a1=int(input("Length of first Rectangle: "))
b1=int(input("Width  first Rectangle: "))
r1=rectangle(a1,b1)

a2=int(input("Length second Rectangle: "))
b2=int(input("Width second Rectangle: "))
r2=rectangle(a2,b2)
if(r1<r2):
    print("Second Rectangle is Larger!!")
else:
    print("First Rectangle is Larger!!")

