str=input("Enter the string:")
ch=str[0]
for c in str[1:-1]:
    if c==ch:
        b=str.replace(c,'$')
print(ch+b[1:])




