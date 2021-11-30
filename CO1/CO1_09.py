#creating string from a string where 1st and last char exchanged
str = input("Enter a String :")
str1 =str[-1:]+str[1:-1]+str[:1]
print("NEW STRING :",str1)