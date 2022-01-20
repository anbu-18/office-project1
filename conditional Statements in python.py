#IF statement

number = int(input("Enter the number: "))
if number %2 ==0:
    print("the number is even")
else:
    print("The number is odd")


#nested if statement

item = "fruits"
fruit = "mango"

if item == "fruits":
    if fruit == "apple":
        print("this fruit is an apple")
    else:
        print("this fruit is not available")

else:
    print("this is not a fruit")
