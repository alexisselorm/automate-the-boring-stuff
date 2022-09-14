    # While Loops
spam = 0
while spam < 5:
    print('Starting again')
    spam += 1
myname = ''
while True:
    print('Please enter your name')
    myname = input()
    if myname == 'Alexis':
        break
print('Thank you')

spam =0
while spam < 5:
    spam+=1
    if spam ==3:
        continue
    print(f'spam is {spam}')