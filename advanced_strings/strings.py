'Hello'

# Escaping
# \n means insert a new line
# \t means insert a tab
# \v means insert a vertical tab
# \f means insert a form feed
# \b means insert a backspace
# \r means insert a carriage return
# \0 means insert a NUL
# \\ means insert a backslash
# r'<something>' is a raw string
r"That is Carol'\s cat"
# Multiline string
new = """
Dear Alexis,
Eve's cat has been arrested for catnapping, curglary at catxtortion
Sincerely
"""
print(new)

# There are some similarities between list and string methods
print(new[0])
print('Dear' in new)

# String methods return a new string since strings are immutable
spam = "Hello world"
print(spam.upper())
print(spam.upper().islower())
print(spam.upper().isupper())

print(spam.lower())
print(spam.lower().isupper())
print(spam.lower().islower())
print(spam)
print('hello'.isalpha())
print('123'.isdecimal())
print('This Is Title Case'.istitle())
print('hello world'.title())
print('Hello world'.startswith('H'))
print('Hello world'.endswith('d'))

print('\n\n'.join(['cats','rats','bats']))
# Split on anything. If no argment is passed to split, the whitespace is used
print('My name is pop'.split())


# Strip
print('            My name is pop              '.strip())
print('     My name is pop    '.lstrip())
print('      My name is pop               '.rstrip())

# Replace string method
print('My name is pop'.replace('pop', 'Alexis'))

# String formatting
name = "Alexis"
place = "Main street"
time="6 pm"
food="turnips"
print(f"Hello {name}, you have been invited to a party at {place},at {time},please bring {food}")