A = int(input("Enter 1st number: "))
B= int(input("Enter 2nd number: "))
C= int(input("Enter 3rd number: "))
if (A > B) and (B > C):largest = A
elif (B > A) and (B > C): largest = B
else:largest = C
print("The largest number is among three number is ",largest)