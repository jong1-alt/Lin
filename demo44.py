s1 = {"A"}
s2 = {}
s3 = set()
s4 = {'A', 'P', 'P', 'L', 'E'}
s5 = set(list('BANANA'))
print(s4)
print(s5)
print(s4 | s5 )
print(s4 & s5)
print(s4 ^ s5)
s4.add('x')
print(s4)
s4.remove('x')
print(s4)
# s4.remove('x')
