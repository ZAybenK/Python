#Find out whether a number received from the user is positive or negative

x = int(input("Enter a number: "))
if x > 0:
    print(str(x) + " is positive")
elif x < 0: 
    print(str(x) + " is negative")
else:
    print(str(x) + " is zero")
    
