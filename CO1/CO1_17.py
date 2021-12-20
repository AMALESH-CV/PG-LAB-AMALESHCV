import operator
d={1:30,2:10,3:20}
print(d)
sort=sorted(d.items(),key=operator.itemgetter(1))
print("dictionary in ascending order by value ",sort)
sort2=sorted(d.items(),key=operator.itemgetter(1),reverse=True)
print("dictionary in descending order value ",sort2)