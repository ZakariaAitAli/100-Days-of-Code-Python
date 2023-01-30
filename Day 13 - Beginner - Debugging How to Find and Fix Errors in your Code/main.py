for number in range(1, 101):
    # or should be and
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    # if should be elif
    elif number % 3 == 0:
        print("Fizz")
    # if should be elif
    elif number % 5 == 0:
        print("Buzz")
    else:
        # This prints a list of number instead of just the number.
        print(number)
