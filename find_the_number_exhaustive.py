# Find the Number
number = input("Enter a number")


if number == 0:
    print ("Number is Zero")
else:
    guess = 0
    while (guess != number):
        guess += 1
        print (guess)
    print ("The number is " , (guess))

