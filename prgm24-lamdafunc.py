x=int(input("Enter the length of the square of  side:"))
area=lambda x:x*x
print("area of square is {0}".format(area(x)))

l=int(input("Enter the length of the rectangle:"))
b=int(input("Enter the breadth of the rectangle:"))
area=lambda l,b:l*b
print("area of rectangle is {0}".format(area(l,b)))

b=int(input("Enter the breath of the triangle:"))
h=int(input("Enter the height of the triangle:"))
area=lambda b,h:0.5*b*h
print("area of the triangle is {0}".format(area(b,h)))