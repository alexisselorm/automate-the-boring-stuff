#!/bin/python3

spams = ['cat', 'bat', 'rat', 'elephant']

# List of lists
spam = [spams, [1, 2, 3, 4, 5, 6, 7], ["Alexis"]]
print(spams[0])

mutable = [10, 20, 30]
mutable[0] = 'Hello'
mutable[1:] = ['World', 'Sweigart']
print(mutable)

del spam[2]

for i in [1, 2, 3, 4]:
    print(i)

  # multiple assignment
cat = ['fat', 'orange', 'loud']
size, colour, disposition = cat
print(size, colour, disposition)

size, colour, disposition = 'skinny', 'black', 'quiet'
print(size, colour, disposition)

# List methods
spams.insert(1, 'moose')
print(spams)

spams.append('koala')
print(spams)

spams.remove('bat')
print(spams)

del spams[0]
print(spams)

spams.sort()
print(spams)


spams.sort(reverse=True,key=str.lower)
print(spams)


def eggs(someParameter:list):
    someParameter.append("Hello")

spa=[1,2,3]
eggs(spa)

print(spa)