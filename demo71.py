def variable_arguements(fix1, fix2, *args):
    print('fix1={}, fix2{}'.format(fix1, fix2))
    for arg in args:
        print('variable part:{}'.format(arg))
variable_arguements("hello",'world')
variable_arguements("hello",'again', 300)
variable_arguements("it is me",'world',300, 3.14, None)

fruits= ['apple', 'banana', 'orange']
variable_arguements('buy some', fruits)
variable_arguements('buy some', *fruits)



