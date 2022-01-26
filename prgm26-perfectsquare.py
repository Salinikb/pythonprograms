l=int(input("Enter the lower limit:"))
u=int(input("Enter the higher limit:"))
x=0
for i in range(l,u+1):
    if i**.5== int(i**.5):
     print(i)