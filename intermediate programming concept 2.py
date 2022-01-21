#If statements

check = "Lion"

if check == False:
    print("it is false")
elif check == "Lion":
    print(" Hey!, there is a lion")
else:
    print("It is actually equal to True")

#For Loop

numbers = [1,2,3,4,5]
for item in numbers:
    print(item)

names = ["anbu","mohan","bharath","giri"]
for name in names:
    print("this is ", name)

#While loop

run = True
current = 1

while run:
    if current == 10:
        run = False

    else:
        print(current)
        current +=1
        
                                            
