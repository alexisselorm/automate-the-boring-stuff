myCat = {'size': 'fat', 'color': 'gray', 'disposition': 'loud'}
print(myCat['size'])

eggs = {'name': 'Zophie', 'species': 'cat', 'age': 8}
'name' in eggs

print(list(eggs.keys()))
print(list(eggs.values()))
print(list(eggs.items()))

for k in eggs.keys():
    print(k)

for k, v in eggs.items():
    print(k, v)


print(eggs.get('color', 'There\'s no colour key'))

if 'color' not in eggs:
    eggs['color'] = 'black'

eggs.setdefault('animal', 'turkey')

print(eggs)

message = 'It was a bright cold day in Xadia, and the dragon price was found. Grr'
count = {}

for char in message.lower():
    count.setdefault(char, 0)
    count[char] += 1

print(count)
