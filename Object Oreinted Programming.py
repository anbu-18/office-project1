class calculator:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b

s=calculator()
r=s.add(5,2)
print(r)


#extended class and methods

class class1:
    var1 = "i am class1"

class class2:
    var2 = "i am class2"

class class3(class1,class2):
    var3 = "i am class3"

obj = class3()
print(obj.var1)
print(obj.var2)
print(obj.var3)
