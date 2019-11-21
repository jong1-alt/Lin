try:
    file = open('data\\testfile1','w')
    print("this is test-exception")
    file.write('write something')
except FileNotFoundError:
    print("something wrong")
else:
    print("file will be closed ")
    file.close()
print("do something else")