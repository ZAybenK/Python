#Finding the absolute value of a number received from the user

x = int(input("Enter a number: "))
if x<0: 
    y = -1 * x
    print("The absolute value of " + str(x) + " is " + str (y))
else:
    print("The absolute value of " + str(x) + " is " + str (x))
    