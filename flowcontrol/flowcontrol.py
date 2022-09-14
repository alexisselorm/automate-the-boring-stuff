# Flow Charts and Basic Flow Control Concepts
print(42 == 41)
print(42 > 41)
print(42 < 41)
print(42 != 41)
print(42 >= 41)
print(42 <= 41)
print(42.0 == 42)

myAge = 88
myPet = 'cat'
print(myAge < 90 and myPet == 'cat')


# If,Else, and Elif Statements
name = 'Alice'
if name == 'Alice':
    print('Hi Alice')
print('done')


password = 'swordfish'
if password == 'password':
    print("Access granted")
else:
    print('Wrong password')

if name == 'Alice':
    print('Hi Alice')
elif myAge < 12:
    print("Who's this kid")
elif myAge > 100:
    print("Dracula?")
else:
    print("Hmm. Weird")

print('Enter a name')
name = input()
if name:
    print('Thank you for signing up')
else:
    print('You did not enter a name')

