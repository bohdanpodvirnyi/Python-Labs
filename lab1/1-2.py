class NegativeNumberException(Exception):

    def __init__(self, value):
        self.value = value


def my_func(a, b):
        print("Result is:", a % b == 0)


if __name__ == "__main__":
    try:
        first_number = int(input("Input first number: "))
        if first_number < 0:
            raise NegativeNumberException(first_number)
        second_number = int(input("Input second number: "))
        if second_number < 0:
            raise NegativeNumberException(second_number)
        my_func(first_number, second_number)
    except NegativeNumberException as exception:
        print("NegativeNumberException occurred: {0} is negative number.".format(exception.value))
