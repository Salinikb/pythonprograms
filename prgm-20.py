start= int(input("Enter the starting:"))
end= int(input("Enter the limit:"))
for num in range(start, end + 1):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                break
        else:
            print(num)