def spam():
    eggs = 99
    bacon()
    print(eggs)


def bacon():
    eggs = 78
    ham = 45


spam()

eggs = 45

print(eggs)


def eggs():
    global eggs
    eggs = 12
    print(eggs)


eggs()
# The 45 eggs in the global scope is changed to 12
print(eggs)
