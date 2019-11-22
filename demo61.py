def factorial(number):
    if not isinstance(number, int):
        raise TypeError("Sorry, number should be integer")
    if not number >= 0:
        raise ValueError("sorry, number should positive")

    def inner_factorial(number):
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)

    return inner_factorial(number)
print(factorial(20))
