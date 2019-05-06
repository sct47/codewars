for i in range(50):
    if i != 0 and i % 3 == 0 and i % 5 == 0:
        print("fizzBuzz")
    elif i != 0 and i % 3 == 0:
        print("fizz")
    elif i != 0 and i % 5 == 0:
        print("Buzz")
    else:
        print(i)

