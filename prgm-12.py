list=[]
n=int(input("Enter the limit:"))
for i in range(n):
    a=int(input("Enter the value:"))
    list.append('over' if a>100 else a)
print("The list with values greater and less than 100:",list)