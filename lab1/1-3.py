import math


class NoSimpleDigitsException(Exception):
    pass


def my_func(a, b):
        return a % b == 0


def find_prime_numbers_in_range(start, end):
    array_of_prime_numbers = []
    try:
        if start <= 1:
            if end < 2:
                raise NoSimpleDigitsException
            else:
                start = 2
    except NoSimpleDigitsException:
        print("NoSimpleDigitsException occurred: there's no simple digits.")
        return
    number = start
    while number != end + 1:
        if is_prime(number):
            array_of_prime_numbers.append(number)
        number += 1
    try:
        if len(array_of_prime_numbers) != 0:
            if 1 in array_of_prime_numbers:
                array_of_prime_numbers.remove(1)
            print("Here is your simple digits: ", array_of_prime_numbers)
        else:
            raise NoSimpleDigitsException
    except NoSimpleDigitsException:
        print("NoSimpleDigitsException occurred: there's no simple digits.")


def is_prime(number):
    for i in range(2, int(math.sqrt(number) + 1)):
        if my_func(number, i):
            return  False
    return True


if __name__ == "__main__":
    first_number = int(input("Input first number: "))
    second_number = int(input("Input second number: "))
    if second_number <= first_number:
        print("Error: incorrect range.")
    else:
        find_prime_numbers_in_range(first_number, second_number)
