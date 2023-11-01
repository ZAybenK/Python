x = int(input("Enter first number: ")) #ask the user for the first number
y = int(input("Enter second numbar: ")) #ask the user for the second number
z = int(input("Enter third number: ")) #ask the user for the third number

#find smallest number
if x<y and x<z:
    print("Smallest number: " + str (x))
elif y<x and y<z:
    print("Smallest number: " + str (y))
else:
    print("Smallest number: " + str (z))
    
#find biggest number
if x>y and x>z:
    print("Biggest number: " + str (x))
elif y>x and y>z:
    print("Biggest number: " + str (y))
else:
    print("Biggest number: " + str (z))
    
#find sum
sum = x+y+z
print("Sum: " + str (sum))

#find multiple
multi = x*y*z
print("Multiple: " + str (multi))

#find average
avg = sum/3
print("Average: " + str (avg))


