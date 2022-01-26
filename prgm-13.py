l=int(input("Enter the num of first names:"))
counts=0
for i in range(l):
    a=str(input("Enter the name:").split(" ")[0])
    counts+=a.count('a')
print(counts)
