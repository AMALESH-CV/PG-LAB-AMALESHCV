f1=open("firstfile.txt","w")   #write mode
f1.write("This is my first file in python\n I am to work with files\n This is my third line")  #writing to the file
f1.close()


f1=open("firstfile.txt","r")
f1.seek(0,0)
ff=f1.readlines()
for x in range (0,len(ff)):
    print(ff[x])

print()
print(ff)
f1.close