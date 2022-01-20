animals =["dog","lion","tiger","bear"]
print(animals)
print(animals[2])
print(animals[-2])

example=[0,1,2,3,4,5,6,7,8,9]
print(example[2:8])
print(example[-5:-1])
print(example[:])

a=[0,1,2,3]
b=[4,5,6,7]
print(a+b)

name="anbu"
print('a' in name)

numbers = [21,30,51,87,65,40]
print(len(numbers))
print(max(numbers))
print(min(numbers))
numbers[2] = 40
print(numbers)

somestring = list("mynameisanbu")
print(somestring)
print(len(somestring))
somestring[8:] = list('love')
print(somestring)

animals =["dog","lion","tiger","bear"]
animals.append('deer')
print(animals)

numbers = [1,1,2,2,3,3,4,5,6,7,8]
print(numbers.count(3))

s=animals+numbers
print(s)

v=numbers.extend(animals)
print(v)

#exercise program
s="my name is anbu"
print('s' in s)

#exercise 2
s="helloworld"
print(s[::-1])


