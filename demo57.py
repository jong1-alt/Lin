def myException(level):
    if level < 1:
        raise Exception('reason', 'detail')
try:
    myException(0)
except Exception as e:
    print(f'exception as {e}')
else:
    print('normal executin')
