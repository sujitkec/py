from random import randint


def greet_random():
    greeting = ['hai', 'hello', 'Namastha', 'Whatsup', "vanakam"]
    n = randint(0, len(greeting))
    return greeting[n-1]
