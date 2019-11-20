l1 = list('ASHJBLQ123456789WEROPXCqwteraitmbml')

def sortByLowercase(x):
    return str.lower(x)


l1.sort()
print(l1)
l1.sort(reverse=True)
print(l1)
l1.sort(key=str.lower)
print(l1)
l1.sort(key=sortByLowercase)
print(l1)

