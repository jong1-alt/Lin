animals = ['aplaca', 'baboon']
def addAnimals(x):
    x.append('zevra')

print(hex(id(animals)),animals)
addAnimals(animals)
print(hex(id(animals)),animals)

animals2 = ('aplaca', 'baboon')

def addAnimal2(x):
    x += ('zebra',)
    print('inside, x={},{},{}'.format(x, y, z))
    print(f'inside, x={x},{y},{z}')
    print('inside, x=%')


print(hex(id(animals2)), animals2)
addAnimal2(animals2)
print(hex(id(animals2)), animals2)
