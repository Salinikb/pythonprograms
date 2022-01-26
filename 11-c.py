Element=input("Enter any word:")
vowels=['a','e','i','o','u']
list=[]
for i in Element:
    if(i in vowels and i not in list):
        list.append(i)
        print("vowels present in given statement:",list)