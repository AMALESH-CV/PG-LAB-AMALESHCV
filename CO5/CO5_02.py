f1=open("firstfile.txt","r")

for x in f1: 
    print(x)
print("________")    
f1.seek(0,0)
ff=f1.readlines()

f2=open("odd.txt","w") #creating a new file for writing the odd lines of file 1

print("\n ODD LINES: \n")
for x in range(0,len(ff)):
    if(x%2==0):
        print(ff[x])
        f2.write(ff[x])
   
f2.close()
        


