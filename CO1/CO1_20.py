num = [7,11, 120, 25, 44, 20, 27,32,8]
print( "Original list:",num)
num = [x for x in num if x%2!=0]
print("list after removing Even numbers:",num)