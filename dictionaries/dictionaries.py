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


# Data Structures

allCats = [{"name":"Zophie","age":7,"color":"gray"},
           {"name":"Pooka","age":5,"color":"black"},
           {"name":"Fat-tail","age":3,"color":"gray"},
           {"name":"Zizzies","age":-1,"color":"orange"},
           ]

theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

theBoard['top-L'] = ' X '
theBoard['top-M'] = ' X '
theBoard['top-R'] = ' X '
theBoard['mid-L'] = ' O '
theBoard['mid-M'] = ' O '
theBoard['low-R'] = ' O '


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('----------')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('----------')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print('----------')


printBoard(theBoard)
