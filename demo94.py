import os

myPath ="c:/windows/system32"

for currentFolder, subFolders, filenames in os.walk(myPath):
    print(currentFolder, subFolders)
    for f in filenames:
        print('F', os.path.join(currentFolder, f))