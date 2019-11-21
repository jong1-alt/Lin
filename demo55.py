try:
    with open('data\\testfile1','w') as file1:
            file1.write("write something")
except:
print("some err...")
# file closed here

