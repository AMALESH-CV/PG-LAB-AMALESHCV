str1 = input("Enter a String :")
ch = str1[0]
str1 = str1.replace(ch, '$')
str1 = ch+ str1[1:]
print("New string is :",str1)