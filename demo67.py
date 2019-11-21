def infinite_gengerator(start=0):
    while True:
        yield start
        start += 2

for num in infinite_gengerator():
    print(num, end=", ")
    if num > 50 :
        break
