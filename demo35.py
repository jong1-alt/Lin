v1 = ['a']
v2 = 'a'
print(v1, v2)
v1[0] ='A'
v2 = 'A'
print(v1, v2)
print(hex(id(v1)), hex(id(v2)))
v1 += ['B']
v2 += 'B'
print(hex(id(v1)), hex(id(v2)))