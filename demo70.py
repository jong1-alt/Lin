def my_oreo(func):
    def wrapper(x):
        print("upper side chocolate")
        func(x)
        print("lower side chocolate")

    return wrapper

@my_oreo
def add_regular_filling(fill):
    print("%s_cream!" % fill)

add_regular_filling('mint-cho')
add_regular_filling('vanilla')