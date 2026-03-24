def get_random_number():
    print("Hi")
    yield 1
    print("Hello")
    yield 7
    print("Howdy")
    yield 4

print(get_random_number())

generator = get_random_number()
next(generator)
next(generator)