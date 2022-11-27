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
