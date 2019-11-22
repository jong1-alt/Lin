try:
    with open('data\\testfile1','w') as file1:
            file1.write("write something")
except:
    print("some error")
# file closed here

try:
    file1 = open('data2\\testfile1','w')
    print("this line may exception")
    file1.write('write something')
except FileNotFoundError:
    print("something wrong")
else:
    print("file will be closed")
    file1.close()
print("do something else")

