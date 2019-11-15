import os
import sys
print(sys.executable)
print(sys.argv)
print(os.getcwd())
for argument in sys.argv:
    print('get an argument:',argument)
