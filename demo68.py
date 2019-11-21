def my_oreo(func):
    def wrapper():
        print("upper side chocolate")
        func()
        print("lower side chocolate")
    return wrapper

def add_filling():
    print("butter_cream!")

get_oreo = my_oreo(add_filling)
get_oreo()
def my_oreo(func):
    def wrapper():
        print("upper side chocolate")
        func()
        print("---lower side chocolate---")

    return wrapper


def add_regular_filling():
    print("butter_cream!")


def add_peanut():
    print("peanut_butter")


fillings = [add_regular_filling, add_peanut, add_peanut,
            add_regular_filling]
for f in fillings:
    get_oreo = my_oreo(f)
    get_oreo()
