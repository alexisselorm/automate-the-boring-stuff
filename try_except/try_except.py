def div42by(divideBy):
    try:
        return 42 / divideBy
    except:
        print("Error: Tried to divide by 0")

print(div42by(2))
print(div42by(4))
print(div42by(5))
print(div42by(0))
print(div42by(18))

print("How many cas do you have")
numCats = input()
try:
    if int(numCats) >= 4:
        print("That is a lot of cats")
    else:
        print("That is not so many cats")
except ValueError:
    print("You did not enter a number")