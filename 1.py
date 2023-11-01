#Finding whether a number received from the user is even or odd

x = int(input("Enter a number: "))
if x % 2 == 0:
    print("The number " + str(x) + " you entered is 'even'")
else:    
    print("The number " + str(x) + " you entered is 'odd'")


"""
print("Girdiğiniz sayi ", 'çift' if int(input("Bir sayi giriniz: ")) % 2 == 0 else 'tek', " bir sayidir.")
"""
