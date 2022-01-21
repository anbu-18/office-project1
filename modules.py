import re
'''
string = ' I am Anbu and I am a " programmer "'
print(string)
new = re.sub('[A-Z]', '', string)
print(new)
new = re.sub('[a-z]', '', string)
print(new)
new = re.sub('[.,\']', '', string)
print(new)
new = re.sub('[.,\'a-zA-Z"]', '', string)
print(new)
'''


#Final project of course 3

print("our Magical Calculator")
print("type 'quit' to exit\n")


previous = 0
run = True

def performMath():
    global run
    global previous
    equation=""
    if previous == 0:
        equation = input("Enter the equtation")
    else:
        equation = input(str(previous))
        
    if equation == "quit":
        print("Goodbye,User.")
        run = False
    else:
        equation = re.sub('[a-zA-Z,.:()" "]','',equation)
        if previous == 0:
            previous = eval(equation)
        else:
            previous = eval(str(previous)+ equation)

while run:
    performMath()
    
