def make_increment(n):
    return lambda x: x+n

f= make_increment(10)
print(f(10), f(20))


def make_increment_detail(n):
    def becomelamda(x):
        return x+n

    return becomelamda

g = make_increment_detail(10)
print(g(10), g(20))

def make_tuple(p):
    return lamda x:(x, 'p' * p)

g2 = make_tuple(5)
print(g2(1), g2(2))