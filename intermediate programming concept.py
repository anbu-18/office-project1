#defining function and calling that function

def my_function():
    print("this is my function!")
    print("hi welcome")

my_function()


#function with an arguments
def function_3(str1,str2):
    print(str1)
    print(str2)

function_3("this is string 1","this is string 2")


#function which passing infinite arguments

def peoples(*people):
    for person in people:
        print("this person is", person)

peoples("anbu","mohan","bharath","giri")


#function using return

def add(num1,num2):
    return num1 + num2

s=add(4,5)
print(s)
